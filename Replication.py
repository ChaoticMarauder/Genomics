def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns

def remove_duplicates(Items):
    ItemsNoDuplicates = [] 
    ItemsNoDuplicates=list(set(Items))
    return ItemsNoDuplicates

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates 

def PatternMatching(Pattern, Genome):
    positions = [] 
    l=len(Genome)
    j=0
    for i in range(l):
        if Pattern==Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions

def SymbolArray(Genome, symbol):
    array = {}
    n=len(Genome)
    ExtendedGenome=Genome+Genome[0:n//2]
    for i in range(n):
        array[i]=PatternCount(symbol,ExtendedGenome[i:i+n//2])
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n=len(Genome)
    ExtendedGenome=Genome+Genome[0:n//2]
    array[0]=PatternCount(symbol,ExtendedGenome[0:n//2])
    for i in range (1,n):
        array[i]=array[i-1]
        if ExtendedGenome[i-1]==symbol:
            array[i]=array[i]-1
        if ExtendedGenome[i+n//2-1]==symbol:
            array[i]=array[i]+1
    return array

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

def MinimumSkew(Genome):
    positions = []
    n=len(Genome)
    skew=Skew(Genome)
    m=min(skew.values())
    for i in range (n+1):
        if skew[i]==m:
            positions.append(i)
    return positions


def MaximumSkew(Genome):
    positions = []
    n=len(Genome)
    skew=Skew(Genome)
    m=max(skew.values())
    for i in range (n+1):
        if skew[i]==m:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    n=len(p)
    count=0
    for i in range (n):
        if p[i]!=q[i]:
            count=count+1 
    return count

def ApproximatePatternMatching(Pattern, Text, d):
    positions = []
    n=len(Text)
    l=len(Pattern)
    for i in range (n-l+1):
        if HammingDistance(Pattern,Text[i:i+l])<=d:
            positions.append(i)
    return positions

def ApproximatePatternCount(Pattern, Text, d):
    count = 0 
    n=len(Text)
    l=len(Pattern)
    for i in range (n-l+1):
        if HammingDistance(Pattern,Text[i:i+l])<=d:
            count=count+1
    return count
