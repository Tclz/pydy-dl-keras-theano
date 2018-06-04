#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
def Arrange(filepath):
    pathdir = os.listdir(filepath)
    # print(pathdir)
    for directory in pathdir:
        print(directory)
        catagory = directory.split('_')[-1]
        print(catagory)
        IsDirectoryExsit(catagory)
        img_list = os.listdir(filepath+directory)
        length = len(img_list)
        size_of_train = int(length*0.8)
        size_of_validation = length - size_of_train
        val_start_index = size_of_train
        val_end_index = val_start_index + size_of_validation

        for img_index in range(size_of_train):
            shutil.move(filepath+directory+'/'+img_list[img_index],'data2/train/'+catagory+'/'+directory+'_'+img_list[img_index])

        for img_index in range(val_start_index,val_end_index):
            shutil.move(filepath+directory+'/'+img_list[img_index],'data2/validation/'+catagory+'/'+directory+'_'+img_list[img_index])



def IsDirectoryExsit(path):
    target_path_train = 'data2/train/'+path
    target_path_validation = 'data2/validation/'+path
    isExists = os.path.exists(target_path_train)
    if isExists:
        return
    else:
        os.makedirs(target_path_train)
        os.makedirs(target_path_validation)


if __name__ == '__main__':
    dataPath = 'data_deepfashion/img/'
    Arrange(dataPath)

