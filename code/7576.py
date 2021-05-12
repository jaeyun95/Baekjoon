#(7576) 토마토

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
box = []
queue = deque()
for _ in range(M):
    box.append(list(map(int,sys.stdin.readline().split(' '))))

moves = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(box,queue):
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            elif box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx,ny])

queue = deque()
for x in range(M):
    for y in range(N):
        if box[x][y] == 1:
            queue.append([x, y])

bfs(box,queue)
day = 0
for i in range(M):
    if 0 in box[i]:
        day = 0
        break
    day = max(day,max(box[i]))
print(day-1)