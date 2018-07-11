# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 03:50:16 2018

@author: Prongs
"""
def expectation(a,b):
    summ=0.0
    for i in range(6):
        summ=summ+a[i]*b[i]
    return 2*summ
        

a=[18471,18739,16059,19349,19618,17005]
prob=[1,1,1,0.75,0.5,0]
print(expectation(a,prob))