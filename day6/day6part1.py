
inputs = []

with open("input.txt","r") as f:
    count = 0
    for line in f:
        count += 1
        inputs.append(line.strip().split())
    print(count)



sign = inputs[-1]
print(len(sign))
print(sign)

res = [False for x in sign]


for i,v in enumerate(sign):
    
    opn = sign[i]

    for j in range(len(inputs)-1):
        if inputs[j][i]:
            if res[i]:
                if opn == "+":
                    res[i] += int(inputs[j][i])
                else:
                    res[i] *= int(inputs[j][i])
                
            else:
                res[i]= int(inputs[j][i])

print(sum(res))