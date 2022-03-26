# Q28(i).

a=[1,1,2,3,4,5,1,2]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]==1:
            a.remove(1)
        j=j+1
    i=i+1
print(a)


# Q28(ii).

a=[5,6,7,8,9,10]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]==7:
            a.remove(7)
        j=j+1
    i=i+1
print(a)
