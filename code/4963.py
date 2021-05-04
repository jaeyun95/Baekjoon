#(4963) 섬의 개수

import sys
from collections import deque

moves = [(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1)]

def bfs(island,x,y):
    queue = deque()
    queue.append((x,y))
    island[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or ny < 0 or nx >= len(island) or ny >= len(island[0]):
                continue
            if island[nx][ny] == 1:
                island[nx][ny] = 0
                queue.append((nx,ny))

while True :
    w, h = map(int, sys.stdin.readline().split())
    island = []
    count = 0
    if w == 0 and h == 0:
        break
    for _ in range(h):
        island.append(list(map(int, sys.stdin.readline().split())))

    for x in range(h):
        for y in range(w):
            if island[x][y] != 0:
                bfs(island,x,y)
                count += 1
    print(count)




