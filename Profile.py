# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:17:16 2018

@author: Prongs
"""

def Profile(text):
    l=len(text)
    dic={'A':[],'C':[],'G':[],'T':[]}
    for i in range(l):
        for j in dic:
            if(text[i]==j):
                dic[j].append(1)
            else:
                dic[j].append(0)
    return dic

l=0
fh=open('rosalind_cons.txt','r')
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
            l=len(sequence)
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
dict[key]=sequence    
dic2={'A':[0]*l,'C':[0]*l,'G':[0]*l,'T':[0]*l}
dic={}
for key in dict:
    dic=Profile(dict[key])
    for key1 in dic2:
        for i in range(l):
            dic2[key1][i]=dic2[key1][i]+dic[key1][i]
#print(dic2)
#print(dict)
for key1 in dic2:
    print(key1,end=':')
    for i in range(l):
        print(dic2[key1][i],end=' ')
    print('\n')
k=""
consensus=""
for i in range(l):
    m=0
    for key1 in dic2:
        if(dic2[key1][i]>m):
            k=key1
            m=dic2[key1][i]
    consensus=consensus+k
print(consensus)        