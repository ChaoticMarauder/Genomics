def HammingDistance(p, q):
    n=len(p)
    count=0
    for i in range (n):
        if p[i]!=q[i]:
            count=count+1 
    return count

p="CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
q="ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
c=HammingDistance(p,q)
print(c)
