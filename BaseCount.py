# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:54:50 2018

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
                
t="ATTGGTTCTGAGAGATCCACAAGTTACGAACTTAGTTCTGGGTCCACTTCGACCCTGAGGTATTCCGCATCACAAATATCTCTAGCAACAAGTAAGAAAGGCGATAAAGGGTATTGGTTGCGCATACTATTGAGTGTGTGCGGTGGGGGAACCGTATGAGGGGTTGACAGCATCATCATCGTATGAAAAACGCGATTAAGTGTTGGGTACCCGTGTACGAGTCTGACTGGGAAAATCCGCGACCGACAGGCAGGCGTACGAACGGTACCGTACTTGCGTCCCATTTATAAGTGCACTTAACCGTCTTCACGAGTAGTGTCATTCCCTAATCTACCGATAGCGAGCAGCAAAGATATACGGCCCTAAGTTCTATGGTTCAGGCAACCCTCAATAGGGACCTCGAGACACCCATGGTAGACGCTTCCTATTACACCGCGACGTGTGACAAGGTCCATCGAAGGCCCGTAATTATTATTCAATTAGCCCTACAAGGTCCAAGTGATGTAGAGCAAGTGCGTCTCTATAACACCGCTGCCGATATTCCCGCCTTAATCACAATCATGATGGTTCTGCCAACCACATATCCTCCAAGAACTATTATATGATTCCCACGGGTGGTCGTGCTATCAAACACGCTCTAGACCAATAGGTTGGACCTGCCTAACGCGGGCCCAGTGCTTAACTTCGCTCACCTCGGGGAATGGCTCCTACCGAATCGGGTCACGAGAGTGTGGTATGTACACTAAGCGTCCAAGGCCGATCTCGTTGTCACTGTTGCCTGCAGAATTTTCGCTGATGGGCTATCGCCGTGCGGAACGATATGAACTGAATAAAACAACATACACGTCGGCAAATACAGAGCGGTGAATCCGCCTTGATGAAAAATCGAG"
print(Base_Count(t))