# -*- coding: utf-8 -*-
"""
Created on Sat May  5 03:24:12 2018

@author: Prongs
"""

def revComplement( t ):
    rev = ''
    for c in t:
        if c == 'A':
            rev = 'T' + rev
        elif c == 'C':
            rev = 'G' + rev
        elif c == 'G':
            rev = 'C' + rev
        elif c == 'T':
            rev = 'A' + rev
    return rev

def isRevPalindrome( text ):
    return text == revComplement(text)

#define dna
fh=open('rosalind_revp (2).txt','r')
line=fh.readline()
sequence=""
while line:
    line=line.rstrip('\n')
    if '>' in line:
        line=fh.readline()
        continue
    else:
        sequence=sequence+line
        line=fh.readline()
for l in range(4,13):
    for i in range(0,len(sequence)-l+1):
        if isRevPalindrome(sequence[i:i+l]):
            print (str(i+1) + ' ' + str(l))