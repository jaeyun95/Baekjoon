#(6087) 레이저 통신

import sys
from collections import deque

W, H = map(int,sys.stdin.readline().split())
visited = [[-1 for _ in range(W)] for _ in range(H)]
maps = []
mirrors = []
for _ in range(H):
    maps.append(list(sys.stdin.readline().rstrip()))

for i in range(H):
    for j in range(W):
        if maps[i][j] == "C": mirrors.append((i,j))

moves = [(0,1),(0,-1),(-1,0),(1,0)]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            while 0 <= nx < H and 0 <= ny < W and maps[nx][ny] != "*":
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                nx, ny = nx + move[0], ny + move[1]

bfs(mirrors[0][0],mirrors[0][1])
print(visited[mirrors[1][0]][mirrors[1][1]]-1)
