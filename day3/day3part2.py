
text_file = "input.txt"

inputlines =[]

with open(text_file,"r") as f:

    for line in f:
        inputlines.append(line.strip())

def find_numbers(path,x,index,res):
    if len(path) == 12:
        res.append(path.copy())
        return 
    for i in range(index,len(x)):
        path.append(x[i])
        find_numbers(path,x,i+1,res)
        path.pop()

def find_numbers_iterative(x):
    res = []
    stack = [(0, [])]  # (start_index, current_path)

    while stack:
        index, path = stack.pop()

        if len(path) == 12:
            res.append(path)
            continue

        # Iterate forward and push next states
        # Reverse range so the leftmost branch is processed first (stack = LIFO)
        for i in range(len(x) - 1, index - 1, -1):
            if len(path) + (len(x) - i) < 12:
                # Not enough elements remaining to reach length 12
                continue
            
            stack.append((i + 1, path + [x[i]]))

    return res

def find_numbers_stack(x):

    stack = []
    res = []
    for i in x:
        while stack and int(stack[-1]) < int(i):
            stack.pop()
        if len(stack) <= 12:
            stack.append(i)
        print(stack)
    return stack


def findnumberslide(x):
    res = []
    left = 0 

    for right in range(11,len(x)):
        while left != right:
            curr = list(x[:right+1])
            temp = curr.pop(left)
            res.append(curr)
            print(curr)
            left += 1
        left += 1
    return res



total_output = 0

for line in inputlines:
    path = []
    res = []
    res = find_numbers_stack("234234234234278")
    print(res)
    total_output += 1
    break

print(find_numbers_heap(line))
print(total_output)