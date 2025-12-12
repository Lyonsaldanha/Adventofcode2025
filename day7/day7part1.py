from collections import deque

inputs = []


with open("input.txt") as f:

    for line in f:
        inputs.append(list(line.strip()))

def go_down(i,j,matrix):
    count = 0
    found = False
    n = len(matrix[0])
    for row in range(i,len(matrix)):
        if  matrix[row][j] == "^":
            found = True
            break
        else:
            matrix[row][j] = "|"
        count += 1
    return (found,count,row,j)

q = deque()
res = 0

i,j = 0,0
for j in range(len(inputs[0])):
    if inputs[0][j] == "S":
        i,j = 0,j
        found,count,row,col = go_down(i,j,inputs)
        if found:
            res += 1
        q.append((row+1,col+1))
        q.append((row+1,col-1))



m,n = len(inputs),len(inputs[0])

visited = set((i,j))
debug = []
while q:
    x,y = q.popleft()
    if (x,y) in visited:
        
        continue
    else:
        visited.add((x,y))
    found,count,row,col = go_down(x,y,inputs)
    if found:
        print(f"Split #{res+1} at row={row}, col={col}")
        if (row,col) in visited:
            continue
        else:
            visited.add((row,col))

        res += 1
        left_col = col - 1
        right_col = col + 1
        

        inputs[row][left_col] = "|"
        q.append((row+1,left_col))
            
    
        inputs[row][right_col] = "|"
        q.append((row+1,right_col))

        


    
i = 0     
    
with open("out.txt","w") as f:
    while i < len(inputs):
        f.write(str(inputs[i]))
        f.write(str("\n"))
        i += 1


print(res)


