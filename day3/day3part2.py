
text_file = "input.txt"

inputlines =[]

with open(text_file,"r") as f:

    for line in f:
        inputlines.append(line.strip())

def find_numbers(path,x,index,res):
    if len(path) == 12:
        curr = ("".join(path))
        res.append(curr)
        return 
    for i in range(index,len(x)):
        path.append(x[i])
        find_numbers(path,x,i+1,res)
        path.pop()




total_output = 0

for line in inputlines:
    path = []
    res = []
    val = find_numbers(path,"234234234234278",0,res)
    print(max(res))

    break

print(total_output)