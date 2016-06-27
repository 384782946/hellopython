# coding:utf-8

import redis

r = redis.Redis(host='23.105.207.220',password='hellomonica',db=0)
if r.ping():
    print '已连接'
else:
    print '连接失败'

#r.set('myname','zxj')
#print r.get('myname')