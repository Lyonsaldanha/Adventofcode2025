from collections import deque

def bfs_grid(mat, start):
    rows, cols = len(mat), len(mat[0])
    q = deque([start])
    visited = {start}
    count = 0 
    level = 2
    dirs8 = [
    (-1, 0),  # up
    ( 1, 0),  # down
    ( 0,-1),  # left
    ( 0, 1),  # right
    (-1,-1),  # up-left
    (-1, 1),  # up-right
    ( 1,-1),  # down-left
    ( 1, 1)   # down-right
    ]   


    while q:

        
        r, c = q.popleft()

        for dr, dc in dirs8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if mat[nr][nc] == "@":
                    count += 1
                if count >= 4:
                    return False
                visited.add((nr, nc))
        q = []
    return True

            

inputgrids = []

with open("input.txt") as f:
    
    for line in f:
        inputgrids.append(list(line.strip()))



ans = 0

def helper(inputgrids):
    ans = 0
    visited = set()
    for i in range(len(inputgrids)):
        for j in range(len(inputgrids[0])):
            if inputgrids[i][j] == "@" and bfs_grid(inputgrids,(i,j)):
                ans += 1
                visited.add((i,j))
    return ans,visited

print(helper(inputgrids))
prev = -1 
curr = 0
i = 0
res = 0
while True:
    curr,visited = helper(inputgrids=inputgrids)

    for r,c in visited:
        inputgrids[r][c] = "."
    print(curr)
    res += curr
    prev = curr
    curr = -1
    i += 1
    if i == 100:
        break
print(res)




