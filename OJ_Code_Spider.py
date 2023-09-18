import requests
import sqlite3
import os
from multiprocessing.pool import Pool
conn=sqlite3.connect('data.db')
cur=conn.cursor()
cur.execute('create table code_id(id varchar(35) primary key,author varchar(40),time varchar(30))')
if not os.path.exists('code'):
    os.mkdir('code')
def save_code(page):
    print(page)
    s=requests.Session()
    s.get('http://114.55.172.240:180/api/submission?id=721375c92da8a545fc79c7dff980760c',headers=headers)
    for i in range(page,page+offset):
        r=requests.get('http://114.55.172.240:180/api/submissions?myself=0&result=&username=&page='+str(i+1)+'&limit=12&offset='+str(i*12))
        for j in r.json()['data']['results']:
            if j['shared']==True:
                cur.execute('insert into code_id(id,author,time)values{0}'.format((j['id'],j['user_id'],j["create_time"])))
                a=s.get('http://114.55.172.240:180/api/submission?id='+j['id']).json()['data']
                file_path1='{0}/{1}.{2}'.format('code',a['id'],'txt')
                if not os.path.exists(file_path1):
                    with open (file_path1,'w',encoding='utf-8')as f:      
                        f.write(a['code'])
                conn.commit()
headers={'X-CSRFToken': 'AzWHbjkhVl4fevGfLg3tMRBXF1NPKHTed52YMsi4IoIRIPq3Se1Lh9RTab1m9rYz',
             'Cookie':'csrftoken=AzWHbjkhVl4fevGfLg3tMRBXF1NPKHTed52YMsi4IoIRIPq3Se1Lh9RTab1m9rYz; sessionid=uhubwrd3mtrv5z4bpf6u4vzlh1dkpiol',
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.95'}
Start=0;End=7232;offset=24
for i in range(Start,End,offset):
    save_code(i)
