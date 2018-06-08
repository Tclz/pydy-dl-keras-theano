#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

# 预测图片类别


def image_prediction():

    result_list =[]
    img_width = 150
    img_height = 150
    model = load_model('../model/multiClassifier-weights-improvement-01-0.384.h5')
    # 待查询图片存放的路径
    path = '../query'
    result =[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
    print(result)
    #names = []
    for index,img_path in enumerate(result):
        img = load_img(img_path,False,target_size=(img_width,img_height))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        print('第'+str(index+1)+'张图片')
       # preds = test_model.predict_classes(x)
        # 获得预测向量
        prediction = model.predict(x)
        #print(prediction)
        # 获得矩阵最大值的索引
        position = np.argmax(prediction)
        #print (position)
        # 取得最大值所在的行，列
        #row, column = divmod(position,5)
        #column = column - 1
        #print(prediction[0][position])
        result_list.append(position)
    return result_list

