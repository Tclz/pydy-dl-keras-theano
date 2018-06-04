#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import pymysql
import re
import time

localhoat = '127.0.0.1'
username = 'root'
passwd = 'root'

def url_open(url):

    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0')
    # opener = urllib.request.build_opener()
    # opener.addheaders = [headers]
    # urllib.request.install_opener(opener)
    result = urllib2.urlopen(url).read().decode("utf-8", "ignore")
    return result


def save_in_db(sql):
    con = pymysql.connect(host=localhoat, user=username, password=passwd, db='test', charset='utf8')
    con.query(sql)
    con.commit()
    con.close()


if __name__ == '__main__':
        # 定义要查询的商品关键词
        keywd_list = ['衬衫','套衫','卫衣', 'T恤','毛衣','polo衫','吊带','睡衣','背心', '夹克', '西装', '大衣','风衣','羽绒服','马甲','披肩','连衣裙','背带裙','中长裤','短裤']
        # print (len(keywd_list))
        for keyword in keywd_list:
            kd = urllib2.quote(keyword)
            # 定义要爬取的页数
            num = 57
            for i in range(num):
                url = "https://s.taobao.com/search?q=" + kd + "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=" + str(i * 44)
                data = url_open(url)
                time.sleep(5)
                # 定义匹配规则
                goods_img = '"pic_url":"(//.*?)"'
                goods_title = '"raw_title":"(.*?)"'
                goods_link = '"detail_url":"(.*?)"'
                goods_price = '"view_price":"(.*?)"'
                goods_fee = '"view_fee":"(.*?)"'
                goods_loc = '"item_loc":"(.*?)"'
                goods_sales = '"view_sales":"(.*?)"'

                # 查找满足匹配规则的内容，并存在列表中
                linkList = re.compile(goods_link).findall(data)
                imgList = re.compile(goods_img).findall(data)
                # print(imgList)
                nameList = re.compile(goods_title).findall(data)
                # print(nameList)
                # print(len(nameList))
                priceList = re.compile(goods_price).findall(data)
                # print(priceList)
                # print(len(priceList))
                feeList = re.compile(goods_fee).findall(data)
                locList = re.compile(goods_loc).findall(data)
                salesList = re.compile(goods_sales).findall(data)

                for n in range(len(linkList)):
                    if not linkList[n].startswith('https'):
                        link = "https:" + linkList[n]
                    else:
                        link = linkList[n]
                    link = link.encode('utf-8').decode('unicode-escape')
                    # link.replace('\\u003d', '=')
                    print(link)
                    img = "http:"+imgList[n]
                    name = nameList[n]
                    price = priceList[n]
                    fee = feeList[n]
                    loc = locList[n]
                    if n < len(salesList):
                      sales = salesList[n]
                    print(keyword)
                    print('正在爬取第' + str(i) + "页，第" + str(n) + "个商品信息...")
                    sql = "insert into goods(name,price,fee,sales,loc,link,img) values('%s','%s','%s','%s','%s','%s','%s')" %(name, price, fee, sales, loc,link,img)
                    save_in_db(sql)
            print("爬取结束")






