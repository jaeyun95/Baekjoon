#(11404) 플로이드

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
distance = [[float("INF") for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int,sys.stdin.readline().split())
    distance[s][e] = min(w,distance[s][e])


for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j: distance[i][j] = 0

for k in range(1,1+n):
    for a in range(1,1+n):
        for b in range(1,1+n):
            distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

for a in range(1,1+n):
    for b in range(1,1+n):
        if distance[a][b] == float("INF"):print(0,end=" ")
        else:print(distance[a][b],end=" ")
    print()
