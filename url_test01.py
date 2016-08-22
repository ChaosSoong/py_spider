import urllib2
import urllib
#re = urllib2.urlopen('http://blog.csdn.net/pleasecallmewhy/article/details/8923067')
#html = re.read()
#print html
url  = 'htt://blog.csdn.net/pleasecallmewhy/article/details/8923067'
values = {'name':'chaos','locatin':'china','lanuage':'python'}
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
print data
req = urllib2.Request(url,data,headers)
try:
    response = urllib2.urlopen(req)
except urllib2.URLError,e:
    print e.reason
the_page = response.read()
print the_page
    
            
    
