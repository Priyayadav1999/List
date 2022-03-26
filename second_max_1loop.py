a=[10,20,30,40,45,47,50,46,49]
i=0
max=0
smax=0
while i<len(a):
    if a[i]>max:
        smax=max
        max=a[i]
    elif a[i]>smax:
        smax=a[i]
    i+=1
print(smax)