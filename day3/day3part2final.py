
text_file = "input.txt"

inputlines =[]

with open(text_file,"r") as f:
    for line in f:
        inputlines.append(line.strip())


def largest_12_digit(s):
    k = 12                          
    remove = len(s) - k               
    stack = []
    
    for ch in s:
        while remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    return ''.join(stack[:k])



total_output = 0
for line in inputlines:
    val = largest_12_digit(line)
    x = int(val)
    total_output += x

print(total_output)
