
dial = [x for x in range(100)]

movements = []

with open("input.txt","r") as f:
    for line in f:
        movements.append(line.strip())

curr = 50
count = 0
test = []

def in_range(left,right):
    return (left < 0 < right)
prev = 50
for m in movements:
    dir = m[0]
    pointer = int(m[1:]) 
    
    if dir == "L":
        pointer *= -1
    prev = curr
    
    curr += pointer 
    curr %= 100
    
    if dial[curr] == 0:
        count += 1
        continue
    if in_range(-prev,curr) or in_range(-curr,prev):
        count += 1
    if pointer > 100:
        count += pointer//100

print(count)