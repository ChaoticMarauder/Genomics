# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:12:06 2018

@author: Prongs
"""

def HammingDistance(s,t):
    l=len(s)
    h=0
    for i in range(l):
        if(s[i]!=t[i]):
            h+=1
        else:
            continue
    return h  
s="ATTAGTACCCCTAGGTGTACTGGTATTCGTTATGTTTTATGGTTGCTTTGTGGTACAGATGTATGCGAGGTGATCCGAACCTTTTAACGATCTGTGTCCAGATGAGGGTGCCACTGACCTTCTTTACCAGGGAATGGACGCCAACCACACCGCCCATGAGTGCACTGTCCCTCATAAGAGCGTCCTTGGGCTACAGTCGACATATAGGTGTAGGATCCGTGACGGCCTGTCCAGGCATCTTTTGAGTGCCTTCGGCGTTACAGTATTGGTAGAGCGCCAATCGTGGCGCGTGTAGCCACTCACTCGTCATTACTGGTACGACGAGCTCCCACACCGTCCTTTACTGAGAACGCCTTTAGCCCCTCGGATGCCGGGCATGGTAACGATCCAGAATGCCACTATTGTAGGTGCATCTTAGTATCTCACATAGCTCGGTTTCAGATCCACAATTTGATAGGCTATATCATATCGAAGGCAGCGGTGCGTAACACTTCTACCAGGTCGGCAGCCCATGCTCGGCCCTGGCTATCCCCCACGTGTTTGACTTGGTAGGAAGGCGGGGCCCGGGTCACCCAGCTTTGCGGCAGTGATCACTGCAGTCGTCTATTGAGTGCTCGCATATCGCTACTAATCCGTTACTATGGTTTACATCCCGGAAGCCTGCATTTTATACTCGTGAATAGCCGATCAGACCACGTGTCAGCGTGGTAGCTAGAAAGTTAAAATAAGCCAGCGGGCAGAGCGTGGGCGGTTAGTGGGGGGTGGACGCGTTGCGATAGATTAGGAGCTGAGTTTACTTGAGTGCTTTGACGTTGGAAACGTCGGTCAAGCGCTGCGGATGTTAACGCATTCAGCGGAGCACATGTTCAACGAGCGGTAAATGGAGATATGTTCTCCATCGACAGCCTAATAATTACTTCGCGTACAAATAGTGTGCCGGTGAGTGTAGTCTGATGGGG"
t="CACACCGCGCCTTGATATTCTAGCGATTACCAGCCACGATCGTGGCCTCGTAGCAGAGCTGTTTTGTAGGTGAGGATCACCGTTAAACATTGTGAGCCCGCAAGATGGATTCACTTGCCGGCTAGTCCTGGCATTCGAGCTCGTCCATAACTGCAAAGAGCTCGAGACCCGTCCAAAGACCGACCTAGGGCTATAATAGACATCAACGAATGGTATCACTGAGGCTGTGGCCAGGCAGCCGAAGCTTGTCCTCGGTATAAGGATCGTTCGGAAAACCGCTTGATACGACCCGTAAGCACTCGCTCTTCGCTGCGGGGACAGCTTAGTCTGATAAAATCCCACACGGGGTTAACAACACGGAGCTGGGGCGGAAGATAACGTAGCCGGTAGGAACACAGCTAGCGTATATGACACTTAGTAACTCCGAACGATCGTCCGCAGATCCATATCTACCAAATTTTTATCACTCGGATTTCAGTGGCATTCCAACCAGCTGTGCTGTCGCGAGCCTATAATGAGCGATACCTGCTGAAGGCCTCATATCTTTAGCCGGATGGATTGCTCGTGGTCACCCCGATTCGCTTCGACCCTATAGGAAACCGTCTATCCAGAGCACGCATGTCGGTACTCGAACGTGCCAGCGACATACAACTGGGTCCCCGACCTTGCGGATCGATAGAGGGGGCGTCAGGCCCCCTGTATATGATTTTGCAGGACAATCAAAATAATTCAACTGACAGATTGTGCGTGCTAAGTAGGGACTGGCAACATACACAATGCCGAAGCGCTGCGCTTACATGAGTGTTATGCACGGGTAACCATATCTAGAGAGCTGGTAATGTTAAACGACTCAGCGGATGGGAGTTTCGAAGTTGTGTGAATCGAAATCTCTCCTACATAGTCATCCTGGGGCTTACCGTCCGCACCCTAAGTCGAACCCTGCGTGTAGTCTATGGACA"
print(HammingDistance(s,t))