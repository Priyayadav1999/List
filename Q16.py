# Q16(i).
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
d=[]
while i<len(a):
    if (i+1)==len(a):
        break
    r=a[i+1]-a[i]
    d.append(r)
    i=i+1
print(d)

# Q16(ii).

a=[2, 4, 6, 8]
i=0
d=[]
while i<len(a):
    if (i+1)==len(a):
        break
    r=a[i+1]-a[i]
    d.append(r)
    i=i+1
print(d)
