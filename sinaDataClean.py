#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:32:20 2019

@author: liuyiquan
"""

import re
import csv
import time
from companyList import company



class newObject:
 def __init__(self,newtime,name,title,desc,url):
        self.newtime = newtime
        self.name = name
        self.title = title
        self.desc = desc
        self.url = url  

output_text=''
companyObj = company()
companyList = companyObj.list

companyListTest = companyObj.testList

p1 = r"(timeNewstime=.*)"
NewstimeF = re.compile(p1)
point1 = r"(:)"
point2 = r"(-)"
titleF = r"\【[^\}]+\】"
titleF = re.compile(titleF)
desc = r"(^(.*?)<)"
descF = re.compile(desc)
urlF = r"(data-url=(\S*))"
urlF = re.compile(urlF)
list = []
for i in companyListTest:
    
    #Open the ordinary text
    filename=str(i)+'.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        context = ''
        for line in f.readlines():
            new = {}
            context = line
            newsTime = re.search(NewstimeF,context)
            newsTime = re.sub(r'[\u4e00-\u9fa5]+','',newsTime.group(0))
            newsday = re.search(point1,newsTime)
            newYe = re.search(point2,newsTime)
            if not newsday and not newYe:
                newData = newsTime.strip('timeNewstime=')
                desc = re.search(descF,context)
                title = re.search(titleF,context)
                if title:
                    title = title.group(0)
                else:
                    title = {}
                url = re.search(urlF,context)
                if url:
                    url = url.group(0).strip('data-url="')
                else:
                    url = {}
                if desc:
                     desc = re.search(descF,context).group(0)
                else:
                    desc = {}
                newtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
                news = newObject(newtime,i,title,desc,url)
                list.append(news)
            
            
        
                
                
                
def info(x):
    
    # time
    newtime = x.newtime
    
    #name
    if x.name :
        name = x.name
    else :
        name = {}
    
    #title
    if x.title:
       title = x.title
    else:
        title = {}
    
    
    
    #获取desc
    if x.desc :
        des = x.desc
    else:
        des = {}
        
    #获取URL
    if x.url :
        url = x.url
    else:
        url = {}
    
    



    info = {
        '时间':newtime,
        '公司名称':name,
        '新闻标题':title,
        '新闻正文':des,
        'URL':url
    }
    return info

headers = ['时间','公司名称','新闻标题','新闻正文','URL']
newList = []
with open('new.csv', 'w', newline='',encoding='utf-8-sig') as f:
     writer = csv.DictWriter(f, headers)
     writer.writeheader()
     for x in list:
         news = info(x)
         newList.append(news)
    
     for row in newList:
        writer.writerow(row)
                
    
            
    