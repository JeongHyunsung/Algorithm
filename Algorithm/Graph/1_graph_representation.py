# Representation of n verticies graph
n = 10
edge_number = 8

## 1. Adjacency matrix
gph1 = [[[False] * n] for _ in range(n)]
for eg in range(edge_number):
    a, b = map(lambda x:int(x)-1, input().split())
    gph1[a][b], gph1[b][a] = True, True

## 2. Adjacency List
gph2 = {}
for i in range(n):
    gph2[i] = []
for eg in range(edge_number):
    a, b = map(lambda x:int(x)-1, input().split())
    gph2[a].append(b)
    gph2[b].append(a)

