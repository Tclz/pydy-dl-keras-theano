#!/usr/bin/env python
# -*- coding: utf-8 -*-

from code import prediction, query_online
import os


def Start():

# 1.默认已经将请求中获取的图片存入query目录下
# 2.图片分类
  image_category_list = prediction.image_prediction()
  print(image_category_list)
  type(image_category_list[0])

# 3. 检索匹配 返回图片id的列表
  path = '../query'
  # 获取query目录下所有待查询图片的名称
  image_name_list =[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
  print(image_name_list)
  for item_index, catergory_index in enumerate(image_category_list):
      image_path = image_name_list[item_index]
      feature_file_index = catergory_index
      similar_img_name_list = query_online.query(img_path=image_path, feature_file_index=2)
      print(similar_img_name_list)
      # 获取每张图片在数据库的id 再根据id来获取详细信息
      img_id =[]
      for item in similar_img_name_list:
          img_id.append(item.split('.')[0])
      print(img_id)
# 4. 根据结果查找数据库，取得相应信息

# 5.结果返回客户端

if __name__ == '__main__':
    Start()
