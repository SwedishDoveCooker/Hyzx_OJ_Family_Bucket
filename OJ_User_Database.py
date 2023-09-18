import requests
import sqlite3
conn=sqlite3.connect('OJ.db')
cursor=conn.cursor()
a='create table data(username varchar(20) primary key,real_name varchar(20),avatar varchar(50),blog varchar(20),mood varchar(256),github varchar(20),school varchar(20),major varchar(20),language varchar(20),accepted_number varchar(20),total_score varchar(20),submission_number varchar(20))'
cursor.execute(a)
for i in range(0,27):
    response=requests.get('http://114.55.172.240:180/api/user_rank?offset='+str(i*30)+'&limit=30&rule=OI')
    for j in response.json()['data']['results']:
        j['username']=j['user']['username']
        j.pop('id')
        j.pop('acm_problems_status')
        j.pop('oi_problems_status')
        j.pop('user')
        #print(str(tuple(j.values())).replace('None',"'无'"))
        try:
            cursor.execute('insert into data{0}values{1}'.format(tuple(j.keys()),str(tuple(j.values())).replace('None',"'无'")))
        except sqlite3.IntegrityError:
            #conn.rollback()
            print(j['username'])
cursor.close()
conn.commit()
conn.close()
n='''200301毕丁骁技7
200626季以勒
200208潘明杰
'''
