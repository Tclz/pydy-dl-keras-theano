# Image Retrieval Engine Based on Keras
## 拍衣得衣 服装检索

### 环境

Keras + Theano + python 2.7

此外需要numpy, os, h5py.推荐使用anaconda安装

### 使用

1.将待输入的图片放在query目录下

2.执行retrieval.py

### 程序执行流程

1.预先对已经分类好的图片数据集提取特征（index.py），特征文件保存在feature目录下.预先训练的分类模型(multi_classifer.py)保存在model目录下.
  预先准备好的数据集，这里采用的是从某电商平台抓取的服装图片（seize.py、resource.py）
  
2.程序获取放在query目录下的文件做为待输入查找的图片

3.调用prediction.py对输入图片进行类别预测

4.将获取到的类别序号作为索引，找到对应的特征文件进行匹配检索（query_online.py).返回一个包含相似图片名称的list.
