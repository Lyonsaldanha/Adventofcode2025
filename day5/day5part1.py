
inputs = []
with open("input.txt","r") as f:
    for line in f:
        inputs.append(line.strip())

def cleaner(inputs):
    Found = False
    ranges,availble = [], []
    for i in inputs:
        if i and not Found:
            split = i.split("-")
            ranges.append(split)
        elif i and Found:
            availble.append(i)
        else:
            Found = True
    return ranges, availble

ranges , available = cleaner(inputs)



fresh = 0
def in_range(x,ranges):
    x = int(x)
    res = False
    for i,j in ranges:
        i = int(i)
        j = int(j)
        if i <= x <= j:
            res = True
    return res


for a in available:
    curr = in_range(a,ranges)
    if curr:
        fresh += 1

print(fresh)