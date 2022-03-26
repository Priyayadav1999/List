a='I am kirti'
g=[ ]
i=0
c=0
while i<len(a):
	if a[i] ==' ':
		c+=1
		g.append('space'+str(c))
	else:
		g.append(a[i])
	i+=1
print(g)