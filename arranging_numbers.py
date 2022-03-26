a=[6, 2, 3, 8]
i=0
max=0
min=a[i]
while i<len(a):
    if a[i]>max:
        max=a[i]
    if min>a[i]:
        min=a[i]
    i=i+1
j=min
b=[]
while j<=max:
    b.append(j)
    j=j+1
print(b)