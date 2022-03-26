a=['Red', 'Maroon', 'Yellow', 'Olive','black']
i=0
b=[]
while i<len(a):
    j=0
    c=[]
    while j<len(a[i]):
        c.append(a[i][j])
        j+=1
    b.append(c)
    i+=1
print(b)