# -*- coding: utf-8 -*-
"""
Created on Fri May  4 00:53:42 2018

@author: Prongs
"""
def RevComp(dna):
    rev=""
    for i in range(len(dna)):
        if dna[i]=='A':
            rev='T'+rev
        elif dna[i]=='T':
            rev='A'+rev
        elif dna[i]=='C':
            rev='G'+rev
        else:
            rev='C'+rev
    return rev

def Rev_Palin(dna):
    return dna==RevComp(dna)

sequence=""
fh=open('rosalind_revp (3).txt','r')
line=fh.readline()
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
        if Rev_Palin(sequence[i:i+l]):
            print(str(i+1) + ' ' + str(l))