# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:51:41 2018

@author: Prongs
"""

def Fib(n,k):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fib(n-1,k)+k*Fib(n-2,k)
    
n=33
k=5
print(Fib(n,k))