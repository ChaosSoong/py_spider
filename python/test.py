#def my_abs(x):
#    if not isinstance(x,(int,float)):
#        raise TypeError('error type')
#    if x>=0:
#        return x
#    else:
#       return -x

#def fact(n):
#   if n==1:
#       return 1
#   else:
#      return n*fact(n-1)

#ecoding=utf-8
#d = {'a':1,'b':2,'c':3}
#for j in d.items():
#   print j
#l=["HEllo","WORLd",18,"coder"]
#l=[s.lower() if isinstance(s,str) else s for s in l ]

#def fib(max):
 #   n, a, b = 0, 0, 1
  #  while n < max:
   #    a, b = b, a + b
    #    n = n + 1
    
#def add(x,y,f):
 #   return f(x)+f(y)
 
#def f1(s):
 #   return s.title()     #s[0].upper()+s[1:].lower()
#print map(f1,['Asdf','DSA','fdsa'])
 
#def sushu(n):
##   j=2
#    while j<n:
#         if n%j==0:
#            return n
#         else:
#             j=j+1
#print filter(sushu,range(1,100))
#md5 = hashlib.md5()
#md5.update("19920501.")
#print md5.hexdigest()
#from urllib2 import request
#with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#    data = f.read()
#    print('status:',f.status,f.reason)
#    for k,v in f.getheader():
#        print('%s: %s'(k,v))
#    print('data:',data.decode('utf-8'))
import socket
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect(('127.0.0.1',9999))
    #print(s.recv(1024).decode('utf-8'))
#for data in [b'Song',b'Wei',b'Chao']:
#    s.send(data)
#    print(s.recv(1024).decode('utf-8'))
#s.send(b'exit')
#s.close()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = r'13313020563@163.com'
password = r'19920501chao'
to_addr = r'1039989645@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('chaos <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()




















































