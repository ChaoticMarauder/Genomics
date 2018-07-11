# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:41:19 2018

@author: Prongs
"""

def Mendel_prob(k,m,n):
    t=k+m+n
    summ=0
    a=[(k/t)*(k-1)/(t-1),2*(k/t)*(m)/(t-1),2*(k/t)*(n)/(t-1),(m/t)*(m-1)/(t-1),2*(m/t)*(n)/(t-1),(n/t)*(n-1)/(t-1)]
    prob=[1,1,1,0.75,0.5,0]
    for i in range(6):
        summ=summ+a[i]*prob[i]
    return summ

print(Mendel_prob(26,15,18))