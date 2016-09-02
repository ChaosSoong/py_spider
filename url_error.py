# -*-coding:utf-8 -*-  
import re
import urllib
import urllib2

class ZHIHU():
    def  __init__(self):
        self.url = 'https://www.zhihu.com/'
        self.agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        self.headers = {'User_Agent': self.agent}
    def getPage(self):
        #print('hehe')
        try:
            request = urllib2.Request(self.url, headers =self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read()
            print(pageCode)
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print('连接知乎失败',e.reason)
                return None
zhihu = ZHIHU()
zhihu.getPage()
        
