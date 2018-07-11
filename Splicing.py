# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:41:48 2018

@author: Prongs
"""

fh=open('rosalind_splc.txt','r')
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
        if(j==0):
            m=line
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

def Translation(text):
    dic = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    protein=""
    l=len(text)
    start=text.find("AUG")
    if start!=-1:
        while start+2<l:
            i=text[start:start+3]
            if (i=="UAA" or i=="UAG" or i=="UGA"):
                break
            for j in dic:
                if(j==i):
                    protein=protein+dic[i]
            start=start+3
    return protein

def Transcription(text):
    length=len(text)
    mRNA=""
    for i in range(length):
        if(text[i]=='T'):
            mRNA=mRNA+'U'
        else:
            mRNA=mRNA+text[i]    
    return mRNA
trans=[]
i=0
DNA=dict.pop(m)
trans.append(DNA)
for k in dict:
    trans.append(trans[i].replace(dict[k],''))
    i+=1
fin=Translation(Transcription(trans[len(trans)-1]))
print(fin)