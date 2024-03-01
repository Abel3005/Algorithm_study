N = 5
nn = [2,3,1,2,2]
answer = 0
nn.sort()
pivot = 0
for i in range(N):
    if (i -pivot + 1) >= nn[i]:
        pivot += nn[i]
        answer +=1
print(pivot)
