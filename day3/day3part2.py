
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

def find_numbers_stack(x):

    stack = []
    res = []
    left = 0
    right = 1
    while int(x[left]) < int(right):
        left += 1
        right += 1
    print(left)
    for v in range(left,len(x)):
        while stack and int(stack[-1]) < int(v):
            res.append(stack.pop())
        if len(stack) <= 12:
            stack.append(x[v])
    print(res)
    return stack

def find_numbers(x):
    res = []
    i = 0
    required_digits = 12
    left = 0 
    right = 0
    maxL = float("-inf")
    while right < len(x):
        if int(x[left]) > maxL:
            maxL = int(x[left])
            print(maxL)
            left += 1
        if (right - left + 1 ) == required_digits:
            res.append(maxL)
            left = left + 1 if left < right else left
            right = right - 1
            maxL = int(x[left])
            required_digits -= 1
        right += 1
        if i == 1000:
            break
        else:
            i+= 1
    print("in here")
    return res

def calc(x):
    cal = 0
    for i in x:
        cal = (cal * 10) + i
    return cal


total_output = 0

for line in inputlines:
    path = []
    res = []
    res = find_numbers("811111111111119")
    print(res)
    break
    val = calc(res)
    total_output += val
    break


print(total_output)