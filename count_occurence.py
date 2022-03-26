list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
empty=[]
while i<len(list):
    count=0
    j=0
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    if [list[i],count] not in empty:
        empty.append([list[i],count])
    i=i+1
print(empty)
