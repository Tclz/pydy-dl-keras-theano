# -*- coding: utf-8 -*-
from extract_cnn_vgg16_keras import VGGNet
import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-query", required = True,
# 	help = "Path to query which contains image to be queried")
# ap.add_argument("-index", required = True,
# 	help = "Path to index")
# ap.add_argument("-result", required = True,
# 	help = "Path for output retrieved images")
# args = vars(ap.parse_args())


# read in indexed images' feature vectors and corresponding image names
feature_file = 'featureCNN.hdf5'
h5f = h5py.File(feature_file, 'r')
feats = h5f['dataset_1'][:]
imgNames = h5f['dataset_2'][:]
h5f.close()
        
print "--------------------------------------------------"
print "               searching starts"
print "--------------------------------------------------"
    
# read and show query image
queryDir = 'database/001_accordion_image_0001.jpg'
queryImg = mpimg.imread(queryDir)
plt.title("Query Image")
plt.imshow(queryImg)
plt.show()

# init VGGNet16 model
model = VGGNet()

# extract query image's feature, compute simlarity score and sort
queryVec = model.extract_feat(queryDir)
scores = np.dot(queryVec, feats.T)
# print(scores)
rank_ID = np.argsort(scores)[::-1]
rank_score = scores[rank_ID]
print rank_ID
print rank_score


# number of top retrieved images to show
maxres = 3
# 既取得索引  又能获取值
imlist = [imgNames[item] for index,item in enumerate(rank_ID[0:maxres])]
# print(imlist)
print "manswear %d images in order are: " %maxres, imlist
 

# show top #maxres retrieved result one by one
for i,im in enumerate(imlist):
    image = mpimg.imread('database'+"/"+im)
    plt.title("search output %d" %(i+1))
    plt.imshow(image)
    plt.show()
