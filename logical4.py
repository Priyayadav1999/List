a=int(input('enter number'))
n=[]
i=1
while i<=a:
	k=[]
	j=1
	while j<=i:
		if a==1:
			print(n)
		elif i>1:
			k.append(j)
		j+=1
	n.append(k)
	i+=1
if a>1:
	print(n)

    
# OUTPUT:- IF INPUT IS GREATER THAN 1 [], [1, 2]

# AND IF INPUT IS 1:-[]