# -*- coding: utf-8 -*-
from code.extract_cnn_vgg16_keras import VGGNet
import numpy as np
import h5py


# ap = argparse.ArgumentParser()
# ap.add_argument("-query", required = True,
# 	help = "Path to query which contains image to be queried")
# ap.add_argument("-index", required = True,
# 	help = "Path to index")
# ap.add_argument("-result", required = True,
# 	help = "Path for output retrieved images")
# args = vars(ap.parse_args())


def query(img_path, feature_file_index):
    # read in indexed images' feature vectors and corresponding image names
    feature_file = '../feature/dl_feature_cnn_'+str(feature_file_index)+'.hdf5'
    h5f = h5py.File(feature_file, 'r')
    feats = h5f['dataset_1'][:]
    img_names = h5f['dataset_2'][:]
    h5f.close()

    print "--------------------------------------------------"
    print "               searching starts"
    print "--------------------------------------------------"

    # read and show query image
    query_dir = img_path
    #queryImg = mpimg.imread(queryDir)
    #plt.title("Query Image")
    #plt.imshow(queryImg)
    #plt.show()

    # init VGGNet16 model
    model = VGGNet()
    # extract query image's feature, compute simlarity score and sort
    # 提取特征并返回该图片特征向量
    query_vec = model.extract_feat(query_dir)
    # 让该特征向量与已有的特征文件中的向量做内积,返回一个一维的数组
    # 每个维度的值在0~1之间 越接近1表示越相似
    scores = np.dot(query_vec, feats.T)
    # print(scores)
    # 返回该数组中元素从高到低排序的索引值
    rank_id = np.argsort(scores)[::-1]
    # 按上面得到的索引重新排序得到新数组
    rank_score = scores[rank_id]
    #print rank_id
    #rank_score


    # number of top retrieved images to show
    maxres = 20
    # 取得索引和值
    imlist = [img_names[item] for index,item in enumerate(rank_id[0:maxres])]
    # print(imlist)
    # print "manswear %d images in order are: " %maxres, imlist
    return imlist

    # show top #maxres retrieved result one by one
    # for i,im in enumerate(imlist):
    #     image = mpimg.imread('data/train/chenshan'+"/"+im)
    #     plt.title("search output %d" %(i+1))
    #     plt.imshow(image)
    #     plt.show()
