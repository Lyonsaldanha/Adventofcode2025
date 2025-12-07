
text_file = "input.txt"

inputlines =[]

with open(text_file,"r") as f:
    for line in f:
        inputlines.append(line.strip())


def largest_12_digit(s):
    k = 12                            # we need exactly 12 digits chosen
    remove = len(s) - k               # how many digits we are allowed to drop
    stack = []
    
    for ch in s:
        while remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    # If we still have extra digits, truncate
    return ''.join(stack[:k])

def calc(x):
    cal = 0
    for i in x:
        cal = (cal * 10) + i
    return cal

total_output = 0
for line in inputlines:
    val = largest_12_digit(line)
    x = int(val)
    total_output += x

print(total_output)
