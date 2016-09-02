# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import cookielib

class HDKY:
    def __init__(self):
        self.loginurl = 'http://219.226.132.31/pls/wwwbks/bks_login2.login'
        self.gradeurl = 'http://219.226.132.31/pls/wwwbks/bkscjcx.yxkc'
        self.cookie = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
                'stuid':'121909020217',
                'pwd':'1992'
            })
        self.headers = {"Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"zh-CN,zh;q=0.8"}
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        self.credit = []
        self.grades = []

    def getPage(self):
        request = urllib2.Request(self.loginurl,self.postdata,headers = self.headers)
        result = self.opener.open(request)
        result = self.opener.open(self.gradeurl)
        return result
        #print(result.read())

    def getGrades(self):
        page = self.getPage().read()
        #print(page)
        pattern = re.compile('''<TR>
<td bgcolor="#EAE2F3"><p align="center">.*?</p></td>
<td bgcolor="#EAE2F3"><p align="center">.*?</p></td>
<td bgcolor="#EAE2F3"><p align="center">.*?</p></td>
<td bgcolor="#EAE2F3"><p align="center">(.*?)</p></td>
<td bgcolor="#EAE2F3"><p align="center">.*?</p></td>
<td bgcolor="#EAE2F3"><p align="center">(.*?)</p></td>
</TR>''',re.S)
        myItems = re.findall(pattern,page)
        for item in myItems:
            if type(item[1])==int:
                print(type(item[1]))
            self.credit.append(item[0])
            self.grades.append(item[1])
        #print(myItems)
        xuefen = 0
        for c in self.credit:
            xuefen +=float(c)
        print u"必修获得学分:",xuefen

if __name__=='__main__':
    hd = HDKY()
    hd.getGrades()
