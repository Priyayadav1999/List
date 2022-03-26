a=[5, 6, [], 3, [], [], 9]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]==[]:
            a.remove([])
        j=j+1
    i=i+1
print(a)
