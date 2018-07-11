# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:15:09 2018

@author: Prongs
"""
import itertools 
fh=open('rosalind_lexf.txt','r')
line=fh.readline().strip('\n')
list=[]
for i in range(len(line)):
    if(line[i]==' '):
        continue
    else:
        list.append(line[i])


order=[]
n=3
for word in itertools.product(list,repeat=n):
   order.append(''.join(word))
   
order.sort()
for i in range(len(order)):
    print(order[i])