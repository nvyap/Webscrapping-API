#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 01:20:32 2018

@author: NavyaPusapati
"""

import requests as req
import json
import sys
#import getopt
from time import sleep


base_url = 'https://api.themoviedb.org/3/discover/movie?api_key='
key1 = sys.argv[1]
key = str(key1)
add_url ='&language=en-US,sort_by=popularity.desc&with_genres=35&primary_release_date.gte=2000-01-01&page='
res = []
i = 1
while len(res)<300:
    a = str(i)
    r = req.get(base_url+key+add_url+a)
    d2=[]
    d = r.json()
    for k in range(len(d['results'])):
        d1=d['results']
        d2.append(d1[k])
    res = res+d2
    i += 1
    sleep(.3)
id1 = ['a']*300
name = ['a']*300
for j in range(300):
    id1[j] = res[j]['id']
    name[j] = res[j]['title']


z = [p for p in zip(id1,name)]
with open('movie_ID_name.csv', 'w') as f:
    for a,b in z:
        f.write(str(a)+","+str(b)+"\n")

base_url2 = 'https://api.themoviedb.org/3/movie/'
add_url2 = '/similar?api_key='
res1 = []
for l in range(len(id1)):
    movie_id = str(id1[l])
    r1 = req.get(base_url2+movie_id+add_url2+key)
    d3 = []
    d4 = r1.json()
    d5 = d4['results'][0:5]
    for k in range(len(d5)):
        #print(d5[k])
        d6 = d5[k]['id']
        x = (int(movie_id),d6)
        d3.append(x)

    res1  += d3
    sleep(.3)

# To remove duplicate items
res2 = []
for (a,b) in res1:
    y = tuple([a,b])
    z = tuple([b,a])
    if y not in res2:
        if z not in res2:
            res2.append(y)
        else:
            if a<b:
                res2.remove(z)
                res2.append(y)


with open('movie_ID_sim_movie_ID.csv', 'w') as f1:
    for a,b in res2:
        f1.write(str(a)+","+str(b)+"\n")
print("Success")

