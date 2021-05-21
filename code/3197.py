#(3197) 백조의 호수

import sys
from collections import deque

R, C = map(int,sys.stdin.readline().split())
lake, swan = [], []
sw_queue, next_sw_queue, water_queue, next_water_queue = deque(), deque(), deque(), deque()
wv = [[False for _ in range(C)] for _ in range(R)]
sv = [[False for _ in range(C)] for _ in range(R)]
for _ in range(R):
    lake.append(list(sys.stdin.readline().rstrip()))

moves = [[0,-1],[0,1],[1,0],[-1,0]]
for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            lake[i][j] = "."
            swan.append((i, j))
        if lake[i][j] == ".":
            water_queue.append((i,j))
            wv[i][j] = True

def melt():
    while water_queue:
        x, y = water_queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < R and 0 <= ny < C and not wv[nx][ny]:
                if lake[nx][ny] == ".":
                    water_queue.append((nx, ny))
                else:
                    next_water_queue.append((nx, ny))
                    lake[nx][ny] = "."
                wv[nx][ny] = True

def met():
    while sw_queue:
        x, y = sw_queue.popleft()
        if x == swan[1][0] and y == swan[1][1]:
            return True
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < R and 0 <= ny < C and not sv[nx][ny]:
                if lake[nx][ny] == ".":
                    sw_queue.append((nx,ny))
                else: next_sw_queue.append((nx,ny))
                sv[nx][ny] = True

    return False

count = 1
sv[swan[0][0]][swan[0][1]] = True
sw_queue.append((swan[0][0],swan[0][1]))
while True:
    melt()
    if met():
        break
    sw_queue = next_sw_queue
    water_queue = next_water_queue
    next_water_queue = deque()
    next_sw_queue = deque()
    count += 1
print(count)
