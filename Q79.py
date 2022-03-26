board = [["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]]
# word = "aaabb"
word="ABCCED"
i=0
while i<len(board):
    j=0
    while j<len(board[i]):
        if board[i][j] in word:
            a="true"
        else:
            a="false"   
        j+=1
    i+=1
print(a)