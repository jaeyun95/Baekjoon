#(1012) 유기농 배추

import sys
from collections import deque

T = int(sys.stdin.readline())
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    visited[x][y] = True
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    maps = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y, x = map(int,sys.stdin.readline().split())
        maps[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0 and not visited[i][j]:
                bfs(i,j)
                count += 1
    print(count)