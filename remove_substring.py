mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
newStr=mainStr.split()
i=0
while i<len(newStr):
    if newStr[i]==subStr:
        newStr.remove(subStr)
    i+=1
print(newStr)
