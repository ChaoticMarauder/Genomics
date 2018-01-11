def Count(Motifs):
    count = {} 
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count={}
    count=Count(Motifs)
    profile=count.copy()
    for symbol in "AGCT":
        for i in range (k):
                    profile[symbol][i]=profile[symbol][i]/10
    return profile

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    score=0
    consensus=Consensus(Motifs)
    l=len(Motifs)
    k=len(Motifs[0])
    for i in range (l):
        for j in range (k):
            if Motifs[i][j]!=consensus[j]:
                score+=1
    return score

def Pr(Text, Profile):
    l=len(Text)
    pr=1.0
    for i in range (l):
        pr=pr*Profile[Text[i]][i]
    return pr
      
