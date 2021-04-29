#(2573) 빙산

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
iceberg = []
for _ in range(N):
    iceberg.append(list(map(int, sys.stdin.readline().split())))

moves = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y,iceberg,visited):
    sea_water = dict()
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if iceberg[nx][ny] == 0:
                sea_water[(x,y)] = sea_water.get((x,y),0)+1
            elif iceberg[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return sea_water

def start():
    time = 0
    while True:
        visited = [[False for _ in range(M)] for _ in range(N)]
        island = 0
        for x in range(N):
            for y in range(M):
                if iceberg[x][y] != 0 and not visited[x][y]:
                    sea_water = bfs(x,y,iceberg,visited)
                    island += 1
        if island >= 2:
            return time
        elif island == 0:
            return 0
        for (x, y), num in sea_water.items():
            if (iceberg[x][y] - num) < 0: iceberg[x][y] = 0
            else: iceberg[x][y] -= num
        time += 1

print(start())
