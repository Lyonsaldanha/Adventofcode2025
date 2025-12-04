
text_file = "input.txt"

inputlines =[]

with open(text_file,"r") as f:

    for line in f:
        inputlines.append(line.strip())



def find_numbers(x):
    left = 0
    val = 0
    maxL = float("-inf")
    for right in range(1,len(x)):
        while left < right:
            maxL = max(maxL,int(x[left]))
            curr =  maxL * 10 + int(x[right])
            if curr > val:
                val =  curr
            left += 1
    return val
            


total_output = 0

for line in inputlines:

    val = find_numbers(line)
    print(val)
    total_output += val
    

print(total_output)