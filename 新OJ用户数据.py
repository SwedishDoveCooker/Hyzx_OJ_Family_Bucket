import re
import requests
import sqlite3
conn=sqlite3.connect('OJ.db')
cursor=conn.cursor()
a='''create table data(_id varchar(5) primary key,uname varchar(10),displayName varchar(5),
avatar varchar(50),bio varchar(80121),qq varchar(10),gender varchar(2),school varchar(20),mail varchar(30))'''
cursor.execute(a)
for i in range(2082):
    va=['_id','uname','displayName','avatar','bio','qq','gender','school','mail']
    result={'_id':'','uname':'','displayName':'','avatar':'','bio':'','qq':'','gender':'','school':'','mail':''}
    a=requests.get('http://www.hzoj.vip:8888/user/'+str(i)).text
    r=re.findall('var UiContextNew = .*;',a)[0]
    b=r[29:-5].split(',')
    for i in b:
        if i.split(':')[0] in va:
            result[i.split(':')[0]]=i.split(':')[1]
    cursor.execute('insert into data{0}values{1}'.format(result.keys(),result.values()))
    db.commit()
'''    try:
        cursor.execute('insert into data{0}values{1}'.format(tuple(j.keys()),str(tuple(j.values())).replace('None',"'无'")))
        db.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        print('err')
 '''   