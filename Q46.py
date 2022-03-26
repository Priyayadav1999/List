a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
i=0
k=[]
while i<len(a):
    j=i
    sum=""
    while j<=i:
        sum=sum+a[i]+b[i]+c[i]
        j+=1
    k.append(sum)
    i+=1
print(k)