import heapq

# n is number of nodes
INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for a in graph[now]:
      if distance[a[0]] > dist + i[1]:
        distance[a[0]] = dist + i[1]
        heapq.heappush(q,(dist+i[1], a[0]))
      
