import requests
#e=0
for i in range(0,27):
    response=requests.get('http://114.55.172.240:180/api/user_rank?offset='+str(i*30)+'&limit=30&rule=OI')
    for j in response.json()['data']['results']:
        a='http://114.55.172.240:180'+j['avatar']
        #print(str(tuple(j.values())).replace('None',"'无'"))
        #if a!='http://114.55.172.240:180/public/avatar/default.png':
        r=requests.get(a)
        with open(j['user']['username']+'.png','wb') as d:
                d.write(r.content)
        print(j['user']['username'])
#        else:
#            e+=1
#print(e)