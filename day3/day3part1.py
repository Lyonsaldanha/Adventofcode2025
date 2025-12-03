
text_file = "input.txt"

inputlines =[]

with open(text_file,"r") as f:

    for line in f:
        inputlines.append(line.strip())



def find_numbers(x):
    left = 0
    n = len(x) 
    val = 0
    for right in range(1,n):
        while left < right:
            curr = int(x[left] + x[right])
            if curr > val:
                val =  curr
            left += 1
        left = 0 
    return val
            


total_output = 0

for line in inputlines:

    val = find_numbers(line)
    print(val)
    total_output += val
    

print(total_output)