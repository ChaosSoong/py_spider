#class Student(object):
#    def __init__(self,name,age):
#        self.age = age
 #   def print_age(self):
 #       print '%s: %s' %(self.name,self.age)
#import sqlite3
#conn = sqlite3.connect('test.db')
#cursor = conn.cursor()
#cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
#cursor.execute('insert into user(id,name)values("3","chao")')
#print(cursor.rowcount)
#cursor.execute('select * from user')
#values = cursor.fetchall()
#print values
#cursor.close()
#conn.commit()
#conn.close()
class People(object):
        #version = '001'
        def __init__(self,name,age):
                self.name = name
                self.age = age
        def hello(self):
                print('hello,name is %s and age is %s'  %(self.name,self.age))

        
