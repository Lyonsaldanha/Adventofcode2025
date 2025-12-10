
inputs = []

with open("input.txt","r") as f:
    count = 0
    for line in f:
        count += 1
        inputs.append(line.strip().split())

sign = inputs[-1]

length = [-1 for _ in range(len(sign))]
res = [False for _ in range(len(sign))]
xlen = len
nmax = max
start = 0
end = 0
maxLen = []

for j in range(len(inputs[0])):
    p1 = xlen(inputs[0][j])
    p2 = xlen(inputs[1][j])
    p3 = xlen(inputs[2][j])
    p4 = xlen(inputs[3][j])
    maxi = nmax(p1,p2,p3,p4)
    maxLen.append(maxi)

print(maxLen)
newinputs = []
with open("input.txt","r") as f:
    for line in f:
        curr = []
        start = 0
        end = 1
        for i in maxLen:
            curr.append(line[start:start+i])
            start = start + i + 1
        
        newinputs.append(curr)
res = [False for _ in range(len(newinputs[0]))]

for j in range(len(newinputs[0])):
    for k in range(maxLen[j]):
        p1 = (newinputs[0][j][k])
        p2 = (newinputs[1][j][k])
        p3 = (newinputs[2][j][k])
        p4 = (newinputs[3][j][k])

        if res[j]:

            if sign[j] == "+":
                res[j] += int(p1+p2+p3+p4)
            else:
                res[j] *= int(p1+p2+p3+p4)
        
        else:
            res[j] = int(p1+p2+p3+p4)

print(res)
print(sum(res))