# Q26(i).
list=[4, 5, 5, 5, 3, 8]
i=0
while i<len(list):
    j=i
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
            if c==3:
                print(list[i])
        j=j+1
    i=i+1

# Q26(ii).

list=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
while i<len(list):
    j=i
    c=0
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        j=j+1
    if c==3:
        print(list[i])
    i=i+1
