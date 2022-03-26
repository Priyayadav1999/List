a=[1,5,7,2,6]
i=0
max=0
while i<len(a):
	if a[i]>max:
		max=a[i]
	i+=1
s_max=0
k=0
while k<len(a):
	if a[k]==max:
		s_max=s_max
	elif a[k]>s_max:
		s_max=a[k]
	k+=1
print(s_max)