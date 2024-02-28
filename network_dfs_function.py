computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3
visited  = [0] * n

def dfs(now):
  if visited[now] == 1:
    return False
  visited[now] = 1
  for i in range(n):
    if visited[i] == 0 and computers[now][i] == 1:
      dfs(i)
  return True
for i in range(n):
  if dfs(i):
    answer += 1
print(answer)
