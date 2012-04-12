#!/usr/bin/env python

import urllib2
import sys
import fbconsole

# uncomment if proxy support required
#fbconsole.PROXY_SUPPORT = urllib2.ProxyHandler({"http" : "http://10.3.11.251:9090"}) 

fbconsole.AUTH_SCOPE = ['user_photos','publish_stream']
fbconsole.authenticate()

albums = fbconsole.get('/me/albums')
alb_id = None
for i in range(len(albums['data'])):
    if albums['data'][i]['name'] == 'Hackathon':
        alb_id = albums['data'][i]['id']
        break

if alb_id == None:
    alb = {'message': 'Hackathon Test','name': 'Hackathon'}
    aid = fbconsole.post('/me/albums',alb)
    alb_id = aid['id']

for i in range(1,len(sys.argv)):
    fbconsole.post('/'+alb_id+'/photos/', {'source':open(sys.argv[i])})


