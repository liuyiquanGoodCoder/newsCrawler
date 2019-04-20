#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:28:42 2019

@author: liuyiquan
"""

from selenium import webdriver
from lxml import etree
import csv

browser=webdriver.Chrome()
url = "https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E6%97%B7%E8%A7%86%E7%A7%91%E6%8A%80"
browser.get(url)
ht = browser.page_source
el = etree.HTML(ht)
xpath_title = '/html/body/div[2]/div[4]/div/div[2]/div[3]/div'
title_path = '/h3/a'
url_path = '/h3/a/@href'
source_path = '/div/p'
desc_path = '/div/text()'
data = el.xpath(desc_path)

def info(x):
    
    # 新闻title
    if el.xpath(xpath_title + '[{}]/h3/a/text()'.format(x))  :
        title = el.xpath(xpath_title + '[{}]/h3/a/text()'.format(x))
        print(title)
    else :
        title = {}

     # 新闻url
    if el.xpath(xpath_title + '[{}]/h3/a/@href'.format(x))  :
        news_url = el.xpath(xpath_title + '[{}]/h3/a/@href'.format(x))
        print(news_url)
    else :
        news_url = {}
    
    #新闻来源
    if el.xpath(xpath_title + '[{}]/div/p'.format(x))  :
        source = el.xpath(xpath_title + '[{}]/div/p/text()'.format(x))
        print(source)
    else :
        source = {}
    
    #描述
    if el.xpath(xpath_title + '[{}]/div/text()'.format(x))  :
       desc = el.xpath(xpath_title + '[{}]/div/text()'.format(x))
       print(desc)
    else:
        desc = {}
    



    info = {
        '新闻标题':title,
        '新闻地址':news_url,
        '新闻来源':source,
        '新闻内容':desc,
    }
    return info

news_list = []
header = ["新闻标题","新闻地址","新闻来源","新闻内容"]
for x in range(1,10):
    news = info(str(x))
    news_list.append(news)

with open('newList.csv','w',newline='',encoding='utf-8-sig') as f:

    writer = csv.DictWriter(f,header)
    writer.writeheader()

    for row in news_list:
        writer.writerow(row)


