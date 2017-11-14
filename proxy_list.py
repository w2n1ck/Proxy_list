#!/usr/bin/env python  
# encoding: utf-8 
"""
author:w2n1ck
blog:byd.w2n1ck.com
"""

import random
import re
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup as bs

config={
        'NUM':10,
        'timeout':5,
        'USER_AGENTS':[
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",]}
headers = {'User-Agent': random.choice(config['USER_AGENTS'])}
proxy = []

def proxy_spider():
    url_xichi = 'http://www.xicidaili.com/nn/'
    r = requests.get(url=url_xichi,headers=headers)
    soup = bs(r.content,'lxml')
    datas = soup.find_all(name='tr',attrs={'class':re.compile('(odd)|()')})
    # print datas
    for data in datas:
        proxys = data.find_all(name='td')
        ip = str(proxys[1].string)
        # ip = 'http://'+ip
        port = str(proxys[2].string)
        type = str(proxys[5].string).lower()
        avail_proxy = proxy_check(ip,port,type)
        if avail_proxy != None:
            return avail_proxy
            # print avail_proxy
def proxy_check(ip,port,type):
    url_check = 'http://ip.chinaz.com/getip.aspx'
    proxylist = {}
    proxylist[type] = '%s:%s' % (ip,port)
    # print proxylist
    try:
        r = requests.get(url=url_check,proxies=proxylist,timeout=5)
        find_ip = re.findall(r'\'(.*?)\'',r.text)[0]
        # print '真实IP：' + find_ip
        if ip == find_ip:
            return proxylist
            # proxy.append(find_ip)
        # print proxy
    except Exception,e:
        pass


proxy_spider()