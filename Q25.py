# Q25(i).
list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8,]
k = 3
i=0
a=[]
while i<len(list):
    j=0
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        if list[i] not in a:
            if k == c:
                a.append(list[i])
        j=j+1
    i=i+1
print(a)

# Q25(ii).

list=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
k = 2
i=0
a=[]
while i<len(list):
    j=0
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        
        if list[i] not in a:
            if c>k:
                a.append(list[i])
        j=j+1
    i=i+1
print(a)
