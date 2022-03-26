a=[2,3,4,5,65,[3,45,56,667],6,7]
for i in  range(len(a)):
    if type(a[i])==list:
        for j in range(len(a[i])):
            print(a[i][j])