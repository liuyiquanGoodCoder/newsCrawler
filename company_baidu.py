#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:28:42 2019

@author: liuyiquan
"""

from selenium import webdriver
from lxml import etree
import csv
import re
import time
from companyList import company
from url import url

browser=webdriver.Chrome()
header = ['时间','公司名称','新闻标题','新闻正文','URL','详细时间','新闻来源']
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
news_list = []
companyObj = company()
companyListTest = companyObj.testList
companyList = companyObj.list
xpath_title = '/html/body/div[2]/div[4]/div/div[2]/div[3]/div'

#引入地址
urlObj = url()
url = urlObj.url


def info(x):
    
    # 新闻title
    if el.xpath(xpath_title + '[{}]/h3/a/text()'.format(x))  :
        title = el.xpath(xpath_title + '[{}]/h3/a/text()'.format(x))
        title = ''.join(str(i) for i in title)
        title = re.sub('[\n]','',title)
        print(title)
    else :
        title = {}

     # 新闻url
    if el.xpath(xpath_title + '[{}]/h3/a/@href'.format(x))  :
        news_url = el.xpath(xpath_title + '[{}]/h3/a/@href'.format(x))
        news_url = ''.join(str(i) for i in news_url)
        print(news_url)
    else :
        news_url = {}
    
    #新闻来源
    if el.xpath(xpath_title + '[{}]/div/p'.format(x))  :
        source = el.xpath(xpath_title + '[{}]/div/p/text()'.format(x))
        source = ''.join(str(i) for i in source)
    elif el.xpath(xpath_title + '[{}]/div/div[2]/p'.format(x)):
        source = el.xpath(xpath_title + '[{}]/div/div[2]/p/text()'.format(x))
        source = ''.join(str(i) for i in source)
    else :
        source = {}
    
    sourceArr = source.split('\n')
    if len(sourceArr) == 4:
        sourceArea = sourceArr[1]
        sourceTime = sourceArr[2]
    else:
        sourceArea = sourceArr[2]
        sourceTime = sourceArr[3]
    print('sourceArea:',sourceArea)
    print('sourceTime:',sourceTime)

    
    
    #描述
    if el.xpath(xpath_title + '[{}]/div/text()'.format(x))  :
       desc = el.xpath(xpath_title + '[{}]/div/text()'.format(x))
       desc = ''.join(str(i) for i in desc)
       print(desc)
       #带有图片的新闻dom结构发生变化，无法取到实际内容，增加内容长度判读。不够完美，需优化
       if len(desc) < 50:
           desc = el.xpath(xpath_title + '[{}]/div/div[2]/text()'.format(x))
           desc = ''.join(str(i) for i in desc)
           print(desc)
    elif el.xpath(xpath_title + '[{}]/div/div[2]/text()'.format(x))  :
       desc = el.xpath(xpath_title + '[{}]/div/div[2]/text()'.format(x))
       desc = ''.join(str(i) for i in desc)
       print(desc)
    else:
        desc = {}
    



    info = {
        '时间':today,
        '公司名称':companyName,
        '新闻标题':title,
        '新闻正文':desc,
        'URL':news_url,
        '详细时间':sourceTime,
        '新闻来源':sourceArea
    }
    return info

for i in companyList:
    time.sleep(0.5)
    companyName = i
    browser.get(url+i)
    ht = browser.page_source
    ht = re.sub('<em>','',ht)
    el = etree.HTML(ht)
    for x in range(1,2):
        news = info(str(x))
        news_list.append(news)

browser.quit()

with open('newList.csv','w',newline='',encoding='utf-8-sig') as f:

    writer = csv.DictWriter(f,header)
    writer.writeheader()

    for row in news_list:
        writer.writerow(row)

