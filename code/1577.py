#(1577) 도로의 개수

import sys

N, M = map(int,sys.stdin.readline().split())
constr = int(sys.stdin.readline())
cache = [[0 for _ in range(N+1)] for _ in range(M+1)]
constr_list = []
for _ in range(constr):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    sx, sy = min(x1,x2), min(y1,y2)
    ex, ey = max(x1,x2), max(y1,y2)
    constr_list.append([sx,sy,ex,ey])

for i in range(1,M+1):
    if [0,i-1,0,i] in constr_list:
        break
    cache[i][0] = 1

for i in range(1,N+1):
    if [i-1,0,i,0] in constr_list:
        break
    cache[0][i] = 1

for x in range(1,M+1):
    for y in range(1,N+1):
        if [y,x-1,y,x] not in constr_list:
            cache[x][y] += cache[x-1][y]
        if [y-1,x,y,x] not in constr_list:
            cache[x][y] += cache[x][y-1]

print(cache[M][N])