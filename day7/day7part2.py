from collections import defaultdict


inputs = []


with open("example.txt") as f:

    for line in f:
        inputs.append(list(line.strip()))

check = inputs.copy()

memo = defaultdict(int)

nlen = len
def go_down(row,col,matrix,res):
    if (row,col) in memo:
        return memo[(row,col)]
    if nlen(matrix) == (row):
        result = 1
        return result
    if matrix[row][col] in (".","S"):
        result = go_down(row+1,col,matrix,res)
        return result
    if matrix[row][col] == "^":
        rleft = go_down(row+1,col-1,matrix,res)
        rright = go_down(row+1,col+1,matrix,res)
        result =  rleft + rright
    memo[(row,col)] = result
    return result

q = []
res = [0]
visited = set()
i,j = 0,0
for j in range(len(inputs[0])):
    if inputs[0][j] == "S":
        i,j = 0,j
        break

print(go_down(i,j,inputs,res))

print(memo)

print(res[0])

