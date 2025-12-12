
ranges = ""

with open("input.txt","r") as f:
    ranges = (f.readline().strip())

ranges = [(lambda i: i.split("-"))(x) for x in ranges.split(",")]


maxR,minR = float("-inf"),float("inf")


for x,y in ranges:
    x = int(x)
    y = int(y)
    if x >= maxR:
        maxR = x
    elif x <= minR:
        minR = x

    if y >= maxR:
        maxR = y
    elif y <= minR:
        minR = y

def invalid(i):
    count = 0
    for x,y in ranges:
        x = int(x)
        y = int(y)
        if (x <= i <= y):
            count += 1
    return count

stored = set()
for i in range(1,100000):

    for j in range(2,11):
        curr = str(i) * (j)
        if curr not in stored:
            stored.add(curr)

res = 0
for x,y in ranges:
    x = int(x)
    y = int(y)
    for s in stored:
        s = int(s)
        if x <= s <= y:
            res += s
            print(s)
print(res)