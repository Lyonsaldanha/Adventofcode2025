
inputs = []
with open("input.txt","r") as f:
    for line in f:
        inputs.append(line.strip())

def cleaner(inputs):
    Found = False
    ranges,availble = [], []
    for i in inputs:
        if i and not Found:
            split = list(map(int,i.split("-")))
            ranges.append(split)
        elif i and Found:
            availble.append(i)
        else:
            Found = True
    return ranges, availble



ranges , available = cleaner(inputs)



def merge_intervals(x,y,hashset):

    if [x,y] not in hashset:
        return 
    for h in hashset.copy():
        i,j = h

        if x <= i <= y:
            if h in hashset:
                hashset.remove(h)
            if [x,y] in hashset:
                hashset.remove([x,y])
            new_i = min(i,x)
            new_j = max(j,y)
            hashset.append([new_i,new_j])
            x, y = new_i, new_j
        elif x <= j <= y:
            if h in hashset:
                hashset.remove(h)
            if [x,y] in hashset:
                hashset.remove([x,y])
            new_i = min(i,x)
            new_j = max(j,y)
            hashset.append([new_i,new_j])
            x, y = new_i, new_j
        elif i <= x <= j:
            if h in hashset:
                hashset.remove(h)
            if [x,y] in hashset:
                hashset.remove([x,y])
            new_i = min(i,x)
            new_j = max(j,y)
            hashset.append([new_i,new_j])
            x, y = new_i, new_j
        elif i <= y <= j:
            if h in hashset:
                hashset.remove(h)
            if [x,y] in hashset:
                hashset.remove([x,y])
            new_i = min(i,x)
            new_j = max(j,y)
            hashset.append([new_i,new_j])
            x, y = new_i, new_j
       


ranges.sort()
hashset = [x for x in ranges]


for i,j in hashset.copy():
    merge_intervals(i,j,hashset)



count = 0


for x,y in hashset:
    count += (y-x) + 1

print(count)