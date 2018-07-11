from itertools import permutations

s = 0
l = []
g = 7 # Input the number you receive in dataset here // or load it through read() 

for x in permutations(range(1,g+1)):
	s+=1
	l.append(x)

f = open('Permutations.txt','w') # Output file

f.write(str(s))
f.write('\n')
for item in l:
		f.write(str(item).replace('(','').replace(',','').replace(')',''))
		f.write('\n')
f.close()