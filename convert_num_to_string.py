a=[23,43,0,4,1,8]
i=0
b=[]
while i<len(a):
    j=0
    sum=""
    y=str(a[i])
    while j<len(y):
        if y[j]=="0":
            sum=sum+"zero"
        elif y[j]=="1":
            sum=sum+"one"
        elif y[j]=="2":
            sum=sum+"two"
        elif y[j]=="3":
            sum=sum+"three"
        elif y[j]=="4":
            sum=sum+"four"
        elif y[j]=="5":
            sum=sum+"five"
        elif y[j]=="6":
            sum=sum+"six"
        elif y[j]=="7":
            sum=sum+"seven"
        elif y[j]=="8":
            sum=sum+"eight"
        elif y[j]=="9":
            sum=sum+"nine"
        j+=1
    b.append(sum)
    i+=1
print(b)

# OUTPUT:- ['twothree', 'fourthree', 'zero', 'four', 'one', 'eight']