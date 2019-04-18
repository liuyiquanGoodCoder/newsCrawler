#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:43:29 2019

@author: liuyiquan
"""

import json
import requests
from companyList import company
import time
import os 


today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
            }
url_head = 'https://m.weibo.cn/api/container/getIndex?luicode=10000011&lfid=100103type%3D1%26q%3D'
url_body = '&containerid=100103type%3D1_7%26t%3D10%26q%3D'
url_tail = '&sudaref=m.weibo.cn&display=0&retcode=6102&page_type=searchall'
pages = 1
companyObj = company()
companyList = companyObj.list

companyListTest = companyObj.testList
fatherPath = os.path.dirname(os.getcwd())
os.mkdir(fatherPath+'/data/txt/'+str(today))
for i in companyList:
    text = []
    url = url_head + i + url_body + i + url_tail
    #print(url)
    filename = fatherPath + '/data/txt/'+str(today)+'/'+str(i)+'.txt'
    print(filename)
    
    
    data = requests.get(url, headers)
    if data:
        data = json.loads(data.content,encoding='utf-8')
        if data['data']['cards']:
            data = data['data']['cards']
            for card in data:
                try:
                    card = card['card_group']
                    for mblog in card:
                        try:
                            mblog = mblog['mblog']
                            if mblog:
                                mblog = mblog['text']+'timeNewstime='+mblog['created_at']
                                print(mblog)
                                text.append(mblog)
                                        
                        except KeyError as e:
                                  print(e)
                except KeyError as e:
                             print(e)
     
    with open(filename,'a',encoding='utf-8') as f:
        for card in text:
            card = str(card)
            f.write(card + '\n')
          
   

        
       
               
               

     

        
        