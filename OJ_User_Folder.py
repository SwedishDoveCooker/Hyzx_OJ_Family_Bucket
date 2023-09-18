import os
import requests
for i in range(0,27):
    response=requests.get('http://114.55.172.240:180/api/user_rank?offset='+str(i*30)+'&limit=30&rule=OI')
    for j in response.json()['data']['results']:
        if not os.path.exists(j['user']['username']):
            os.mkdir(j['user']['username'])
        r_avatar=requests.get('http://114.55.172.240:180'+j['avatar'])
        file_path1='{0}/{1}.{2}'.format(j['user']['username'],'avatar','png')
        print('done')
        if not os.path.exists(file_path1):
            with open (file_path1,'wb')as f:
                f.write(r_avatar.content)
        file_path2='{0}/{1}.{2}'.format(j['user']['username'],'user','txt')
        if not os.path.exists(file_path2):
            with open (file_path2,'w',encoding='utf-8')as f:
                f.write(j['user']['username'])
                j.pop('acm_problems_status')
                j.pop('oi_problems_status')
                j.pop('user')
                for k in j:
                    f.write(k+' : '+str(j[k])+'\n')
