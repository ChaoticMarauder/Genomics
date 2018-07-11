# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:22:29 2018

@author: Prongs
"""

def adjacency_check(s,t):
    l=len(s)
    if s!=t:
        if(s[l-3:]==t[:3]):
            return True
        else:
            return False
    else:
        return False
        
fh=open('rosalind_grph (1).txt','r')
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
for k in dict:
    for j in dict:
        if adjacency_check(dict[k],dict[j]):
            print(k[1:]+' '+j[1:])
