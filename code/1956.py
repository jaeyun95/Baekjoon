#(1956) 운동

import sys

V, E = map(int,sys.stdin.readline().split())
distance = [[float("INF") for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    distance[a][b] = c

for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            distance[a][b] = min(distance[a][b],distance[a][k]+distance[k][b])

dis = float("INF")
for a in range(1,V+1):
    if not distance[a][b] == 0:
        dis = min(distance[a][a],dis)

if dis == float("INF"): print(-1)
else: print(dis)
