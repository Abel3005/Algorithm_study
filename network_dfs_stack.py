computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3

answer = 0
visited = [0] * n
stack = []
for i in range(n):
  if visited[i] == 0:
    answer += 1
    stack.append(i)
    visited[i] = 1
    while stack:
      now = stack.pop()
      for j in range(n):
        if visited[j] == 0 and computers[now][j] == 1:
          stack.append(j)
          visited[j] = 1
print(answer)
