
dial = [x for x in range(100)]

movements = []

with open("input.txt","r") as f:
    for line in f:
        movements.append(line.strip())

curr = 50
count = 0
test = []

for m in movements:
    dir = m[0]
    pointer = int(m[1:]) 
    sign = 1
    if dir == "L":
        sign = -1
    for i in range(1,(pointer)+1):
        curr += (1*sign)
        curr %= 100
        if dial[curr] == 0:
            count += 1

print(count)

    