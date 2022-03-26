i=1
p_count=0
space_count=i
l1=[]
l2=[]
while i>0:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        p_count+=1
        l1.append(i)
        space_count=i-space_count
        l2.append(space_count)
        space_count=i

    if p_count==100:
        break

    i+=1
print(l2) 
