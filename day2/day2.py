
ranges = ""

with open("input.txt","r") as f:
    ranges = (f.readline().strip())

ranges = [(lambda i: i.split("-"))(x) for x in ranges.split(",")]


stored = set()
for i in range(1,100000):

    curr = str(i) * 2
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