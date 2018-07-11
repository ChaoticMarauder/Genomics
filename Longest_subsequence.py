# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:05:55 2018

@author: Prongs
"""
lis=[]
value_list=[]
get_values=input()
value_list=get_values.split()
l=len(value_list)

for i in range(l):
    lis.append(int(value_list[i]))
    
inc_list=[]
dec_list=[]
ti=[]
td=[]
j=0
while j<l:
    ti.append[lis[j]]
    if(lis[j]<lis[j+1]):
        ti.append[lis[j+1]]
    else:
        if(len(inc_list)>ti):
            inc_list=ti
        ti=[]
    j=j+1
    
while j<l:
    td.append[lis[j]]
    if(lis[j]>lis[j+1]):
        td.append[lis[j+1]]
    else:
        if(len(dec_list)>td):    
            dec_list=td
        td=[]
    j=j+1

for i in range(len(inc_list)):
    print(inc_list[i]+" ")
for i in range(len(dec_list)):
    print(dec_list[i]+" ")