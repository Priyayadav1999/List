a=[[10,2,15],[14,15,19]]
n=[]
# k=[]
i=0
while i<len(a):
    k=[]
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    k.append(sum)
    i=i+1
    n.append(k)
print(n)
