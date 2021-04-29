#(2178) 미로 탐색

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(list(map(int,list(sys.stdin.readline().rstrip()))))
moves = [[1,0],[-1,0],[0,1],[0,-1]]
x, y = 0, 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[N-1][M-1]

print(bfs(x,y))