# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 04:30:21 2018

@author: Prongs
"""
#Really slow though took around 170 seconds to get it done
fh=open('rosalind_lcsm.txt','r')
line=fh.readline()
dict={}    
j=0
key=''
sequence=''
while line:
    line=line.rstrip('\n')
    if '>' in line:
        if(key!=''):
            dict[key]=sequence
            j+=1
        key=line
        line=fh.readline()
    else:
        sequence=sequence+line
        line=fh.readline()
        continue
    if len(dict)>j:
        key=''
    sequence=''
#print(dict)
dict[key]=sequence
l=len(sequence)

a=[]
for i in range(l):
    for j in range(i+1,l):
        a.append(sequence[i:j])

for k in dict:
    while i<len(a):
        if(dict[k].find(a[i])==-1):
            a.remove(a[i])
            continue
        i+=1
    i=0

maxx=0
for m in range(len(a)):
    if(len(a[m])>maxx):
        maxx=len(a[m])
k=0
while k<len(a):
    if(len(a[k])<maxx):
        a.remove(a[k])
        continue
    k+=1
    
    
print(a)