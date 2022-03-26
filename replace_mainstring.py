mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on"
newStr=mainStr.split()
i=0
while i<len(newStr):
    if newStr[i]==subStr:
        newStr[i]=replacementStr
    i+=1
print(newStr)
