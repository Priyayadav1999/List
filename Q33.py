
# Q33(i).

a= [12, 67, 98, 34]
i=0
k=[]
while i<len(a):
    sum=0
    while a[i]>0:
        r=a[i]%10
        sum=sum+r
        a[i]//=10
    k.append(sum)
    i=i+1
print(k)

# Q33(ii).

a= [15, 81, 11, 234]

i=0
k=[]
while i<len(a):
    sum=0
    while a[i]>0:
        r=a[i]%10
        sum=sum+r
        a[i]//=10
    k.append(sum)
    i=i+1
print(k)

