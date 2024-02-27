import heapq
INF = int(1e9)
def solution(n, costs):
    answer = 0
    #graph: n*n 
    graph = [[INF] * n for _ in range(n)]
    #print(graph)
    for i in costs:
        a,b,c = i
        graph[a][b] = c
        graph[b][a] = c
    visited = [0]
    for i in range(n):
        graph[i][0] = INF
    while len(visited) < n:
        minv, minid = INF,-1
        for i in visited:
            t = min(graph[i])
            if t < minv:
                minv = t
                minid = graph[i].index(t)
        visited.append(minid)
        answer += minv
        #print(minid)
        for i in range(n):
            graph[i][minid] = INF
    return answer
