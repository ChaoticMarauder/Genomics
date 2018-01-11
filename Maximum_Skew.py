def Skew(Genome):
    skew = {} 
    n=len(Genome)
    skew[0]=0;
    for i in range (1,n+1):
        if Genome[i-1]=="C":
            skew[i]=skew[i-1]-1
        elif Genome[i-1]=="G":
            skew[i]=skew[i-1]+1
        else:
            skew[i]=skew[i-1]
    return skew

def MaximumSkew(Genome):
    positions = []
    n=len(Genome)
    skew=Skew(Genome)
    m=max(skew.values())
    for i in range (n+1):
        if skew[i]==m:
            positions.append(i)
    return positions

s="CATTCCAGTACTTCGATGATGGCGTGAAGA"
pos=MaximumSkew(s)
print(pos)
