# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 01:42:11 2018

@author: Prongs
"""

def Base_Count(text):
    length=len(text)
    dict ={'A':0,'C':0,'G':0,'T':0}
    for i in range(length):
        for j in dict:
            if text[i]==j:
                dict[j]+=1
    return dict

def GC_content(text):
    l=len(text)
    dict=Base_Count(text)
    GC=dict['G']+dict['C']
    content=(GC/l)*100.0
    return content

fh=open('rosalind_gc (1).txt','r')
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

max_gc=0.0
max_id=''
for i in dict:
    if GC_content(dict[i])>max_gc:
        max_gc=GC_content(dict[i])
        max_id=i
    else:
        continue
print(max_id)
print(max_gc)