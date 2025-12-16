import math
from collections import defaultdict 
import heapq


junction_boxes = []

with open("example.txt","r") as f:
    
    for line in f:
        junction_boxes.append(list(map(int,line.strip().split(","))))


hashtable =  defaultdict(lambda:math.inf)
l1 = []
x = 0
for i in junction_boxes:
    mini = None
    curr_j = None
    curr_i = None
    for j in junction_boxes:
        if i == j:
            continue

        x1,x2,x3 = i
        y1,y2,y3 = j
    
        curr_dist = math.sqrt(((x1-y1) ** 2) + ((x2-y2) ** 2) + ((x3-y3) ** 2))
        if not mini and  not curr_i and not curr_j:
            mini = curr_dist
            curr_j = j
            curr_i = i
        elif mini > curr_dist:
            mini,curr_j,curr_i = curr_dist,j,i
    print((mini,curr_j,curr_i))
    l1.append((mini,curr_j,curr_i))



heapq.heapify(l1)

new_list = []

for i in range(len(l1)):
    dist,x,y= heapq.heappop(l1)
    Found = False
    for curr in new_list:
        if x in curr or y in curr:
            Found = curr
            break
    if not Found:
        new_list.append([x,y])
    else:
        if x in Found and y in Found:
            continue
        elif x not in Found and y in Found:
            Found.append(x)
        elif x in Found and y not in Found:
            Found.append(y)
        Found = None



curr = sorted(new_list,key=len,reverse=True)

test = curr[:3]
res = 1

print([len(t) for t in test])

for t in test:
    res *= len(t)
print(res)