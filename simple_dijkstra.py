#simple dijkstra algorithm
# graph shape is list [(b1,c1) .. (bn, cn)], its number of element is a
# b means other node except itslef, and c means cost to go other node
# n is number of nodes
INF = int(1e9)
distance = [INF] * (n+1)

def get_smallest_node():
  index = 0
  minvalue = INF
  for i in range(1,n+1):
    if not visited and minvalue < distance[i]:
      minvalue = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for a in graph(start):
    distance[a[0]] = a[1]
  for _ in range(n-1):
    now = get_smallest_number()
    visited[now] = True
    for i in graph[now]:
      if distance[i[0]] > distance[now] + i[1]:
        distance[i[0]] = distance[now] + i[1]

