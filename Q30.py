# Q30(i).

list1 = [2, -7, 5, -64, -14]
i=0
c_pos=0
c_neg=0
while i<len(list1):
    if list1[i]>0:
        c_pos+=1
    if list1[i]<0:
        c_neg+=1
    i=i+1
print("positive numbers count=",c_pos)
print("negative numbers count=",c_neg)


# Q30(ii).

list1 =[-12, 14, 95, 3]


i=0
c_pos=0
c_neg=0
while i<len(list1):
    if list1[i]>0:
        c_pos+=1
    if list1[i]<0:
        c_neg+=1
    i=i+1
print("positive numbers count=",c_pos)
print("negative numbers count=",c_neg)
