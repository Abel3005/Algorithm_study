vals = [12,3,41,342,52,32,4,5,33]
n = 9

k = [[] for _ in vals]
l = [0 for _ in vals]
s = []
for i in vals:
    k[i%n].append(i)
print(k)
for i in range(len(k)):
    if k[i]:
        minV = "9999"
        for j in k[i]:
            minV = str(j) if minV > str(j) else minV
        for j in k[i]:
            if int(minV) == j:
                l[i] = j
            else:
                s.append(j)
s.sort()
count =0
for i in range(len(l)):
    if l[i] == 0:
        l[i] = s[count]
        count+=1
answer = l
