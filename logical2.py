n=3
a=[]
k=1
while k<=n:
    list=["A","B"]
    i=0
    sum=""
    while  i<len(list):
        a.append(list[i]+str(k))
        i+=1
    k+=1
print(a)


# OUTPUT:- A1,B1,A2,B2,A3,B3