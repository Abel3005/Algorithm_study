n = 4
m = 7
edges = [
    [1,2,4],
    [1,4,6],
    [2,1,3],
    [2,3,7],
    [3,1,5],
    [3,4,4],
    [4,3,2]
]
INF = int(1e9)
graph = [ [INF] * (n+1) for i in range(n+1) ]
for i in range(1,n+1):
    graph[i][i] = 0
for e in edges:
    a,b,c = e
    graph[a][b] = c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])

print(graph)
