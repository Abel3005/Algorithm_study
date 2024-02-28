M = 15
N =2
S = [2,3]

d = [10001] * (M+1)
d[0] = 0

for i in range(N):
  for j in range(S[i],M+1):
    d[j] = min(d[j],d[j-S[i]] +1)
answer = d[M] if d[M] != 10001 else -1
