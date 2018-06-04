# -*- coding: utf-8 -*-
import os
import h5py
import numpy as np
import argparse

from extract_cnn_vgg16_keras import VGGNet

# ap = argparse.ArgumentParser()
# ap.add_argument("-database", required = True,
# 	help = "Path to database which contains images to be indexed")
# ap.add_argument("-index", required = True,
# 	help = "Name of index file")
# args = vars(ap.parse_args())


'''
 Returns a list of filenames for all jpg images in a directory. 
'''


def get_imlist(path):
    result =[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
    print result
    return result


'''
 Extract features and index the images
'''
if __name__ == "__main__":

    # db = args["database"]
    db = 'database'
    output = 'featureCNN.hdf5'
    img_list = get_imlist(db)
    
    print "--------------------------------------------------"
    print "         feature extraction starts"
    print "--------------------------------------------------"
    
    feats = []
    names = []

    model = VGGNet()
    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feat(img_path)
        # 以 "PATH" 中最后一个 '/' 作为分隔符，分隔后，将索引为0的视为目录（路径），将索引为1的视为文件名
        img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_name)
        print "extracting feature from image No. %d , %d images in total" % ((i+1), len(img_list))

    feats = np.array(feats)
    # directory for storing extracted features

    print "--------------------------------------------------"
    print "      writing feature extraction results ..."
    print "--------------------------------------------------"
    
    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_1', data=feats)
    h5f.create_dataset('dataset_2', data=names)
    h5f.close()

    print " write features into file ends."
