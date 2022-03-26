num=[10,23,4,5,6,67,76,34,12]
i=0
while i<len(num):
    j=0
    while j<len(num):
        if num[i]<num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
        j+=1
    i+=1
print(num)