# -*- coding: utf-8 -*-
#try:
#    f=open('C:/Users/djj/Desktop/0425.txt','r')
#    for line in f.readlines():
#        print(line.strip())
#finally:
#   if f:
#        f.close()
#s='0'
#n=int(s)
#print 10/n
#import json
#d=dict(name='bob',age=20,score=88)
#json.dumps(d)
#import os
#print 'Process (%s) start...' %os.getpid()
#pid=os.fork()
#if pid==0:
#    print'I am child process (%s) and my parent is %s.' %(os.getpid(),os.getppid())
#else:
#    print'I (%s) just created a child process (%s)' %(o.getpid(),pid)
import re
p=re.match(r'^(\w+)@(\w+\.(com)|(org))$','qw@123.com')
if re.match(r'(^\w+)@(\w+)\.((com)|(org))','qw@123.com'):
    print 'ok'
else:
    print 'error'
print p.group(0)
print p.group(1)
print p.group(2)
