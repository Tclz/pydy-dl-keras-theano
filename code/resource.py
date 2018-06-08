#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import urllib2
import time

localhoat = '127.0.0.1'
username = 'root'
passwd = 'root'
cnt = 47501


def url_open(url):
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
    result = urllib2.urlopen(url).read()
    # result = request.urlopen(page).read()
    return result


def save_img(img):
        global cnt

        print('正在获取第'+str(cnt)+'张图片')
        with open('../img/duanku/'+str(cnt)+'.jpg', 'wb') as fn:
            fn.write(img)
        cnt += 1


def get_img():
    con = pymysql.connect(host=localhoat, user=username, password=passwd, db='test', charset='utf8')
    # 查询sql语句
    sql = "select img from goods where id > 47500"
    # 使用cursor()方法获取操作游标
    cursor = con.cursor()

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # print(results)
    for img_url in results:
        # print(img_url)
        url = str(img_url)
        target_url = url[3:len(url)-3]
        print(target_url)
        img = url_open(target_url)
        save_img(img)
    cursor.close()
    con.close()


if __name__ == '__main__':
    get_img()

