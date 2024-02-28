n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def find(parents, a):
    if parents[a] == a:
        return a
    else:
        return find(parents, parents[a])
def union(parents,a,b):
    rootA = find(parents,a)
    rootB = find(parents,b)
    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB
    return
answer = 0
costs.sort(key=lambda x : x[2])
parents = [i for i in range(n)]
for e in costs:
    a,b,c = e
    if find(parents,a) != find(parents,b):
        union(parents,a,b)
        answer += c
print(answer)