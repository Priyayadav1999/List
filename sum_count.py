number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
empty=[]
k=0
while i<len(n):
    j=i
    while j<len(n):
        if n[i]+n[j]==number:
            empty.append([])
            empty[k].append(n[i])
            empty[k].append(n[j])
            k=k+1
        j=j+1
    i=i+1
print(empty)


# METHOD 2

number=30
n=[10,11,12,13,14,17,18,19]
i=0
k=[]
while i<len(n):
    a=[]
    j=i
    sum=0
    while j<len(n):
        if n[i]+n[j]==number:
            a.append(n[i])
            a.append(n[j])
            k.append(a)
        j=j+1
    i=i+1
print(k)
