#coding:utf-8
import urllib2
import urllib
import re
import time
from random import choice

iplist = ['1.9.189.65:3128','27.24.158.130:80','27.24.158.154:80']


list1 = ['小鱼','厦门','科技']
for item in list1:
    keyword = item
    ip = choice(iplist)
    # proxy_support = urllib2.ProxyHandler({'http':'http://' + ip})
    # opener = urllib2.build_opener(proxy_support)
    # urllib2.install_opener(opener)

    # print keyword
    url = "http://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word=" + urllib.quote(keyword)
    headers = {
    'GET':url,
    'Host':'sug.so.360.cn',
    'Referer':'http://www.so.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
    }

    req = urllib2.Request(url)
    for key in headers:
        req.add_header(key, headers[key])

    html = urllib2.urlopen(req).read()

    f = open("1.txt","a");
    returnItem = eval(html[12:-2])
    f.write("关键字：" + keyword + "\n")
    for item in returnItem['result']:
        f.write(item['word'] + "\n")
    f.close()

    time.sleep(1)