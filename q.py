nums = [1,1,2]
i=0
a=[]
b=[]
k=0
while i<len(nums):
    if nums[i] not in a:
        a.append(nums[i])
        k+=1
    elif nums[i] in a:
        nums[i]="_"
        b.append(nums[i])
    i=i+1
a.extend(b)
print(k,", nums=",a)