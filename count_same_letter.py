k=['abe','aba','dad']
i=0
k[i].split()
count=0
while i<len(k):
	j=0
	a=k[i][j]
	while j<len(k[i]):
		j=j+1
	if a==(k[i][j-1]):
		count+=1
	i+=1
print(count)
