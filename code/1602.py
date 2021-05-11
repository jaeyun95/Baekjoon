#(1602) 도망자 원숭이

import sys

N, M, Q = map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))
connect = [[float("INF") for _ in range(N+1)] for _ in range(N+1)]
plus_bother = [[float("INF") for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, sys.stdin.readline().split())
    connect[a][b] = d
    connect[b][a] = d
    plus_bother[a][b] = d + max(time[a-1],time[b-1])
    plus_bother[b][a] = d + max(time[a-1],time[b-1])

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            connect[i][j] = 0
            plus_bother[i][j] = 0

time_list = []
for i, t in enumerate(time):
    time_list.append([i+1,t])
time_list.sort(key=lambda x:x[1])

for k in range(1,N+1):
    idx = time_list[k-1][0]
    for a in range(1,N+1):
        for b in range(1,N+1):
            connect[a][b] = min(connect[a][b],connect[a][idx]+connect[idx][b])
            plus_bother[a][b] = min(plus_bother[a][b], connect[a][b] + max(time[a-1],time[idx-1],time[b-1]))

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    if plus_bother[a][b] != float("INF"):
        print(plus_bother[a][b])
    else: print(-1)

