#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:28:42 2019

@author: liuyiquan
"""

#from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from lxml import etree

browser=webdriver.Chrome()
browser=webdriver.Chrome()
url = "https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E6%97%B7%E8%A7%86%E7%A7%91%E6%8A%80"
browser.get(url)
ht = browser.page_source
conut1 = len('<?xml version="1.0" encoding="UTF-8"?>')
et = etree.HTML(ht)
path = '/html/body/div[2]/div[4]/div/div[2]/div[3]/div/h3/a'
#content = et.xpath(path)
data = et.xpath(path)
print(data)
for i in data:
    print(i.text)
