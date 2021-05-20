#(4991) 로봇 청소기

import sys
from collections import deque
from itertools import permutations

moves = [(0,1),(0,-1),(-1,0),(1,0)]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited = [[0 for _ in range(w)] for _ in range(h)]
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if maps[nx][ny] != "x":
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited

while True:
    w, h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0: break
    flag = True
    maps, robot, dusts = [], [], []
    for i in range(h):
        row = list(sys.stdin.readline().rstrip())
        maps.append(row)
        if "o" in row: robot = [i,row.index("o")]
        if "*" in row:
            for j in range(w):
                if row[j] == "*":
                    dusts.append([i,j])

    distance = [[0 for _ in range(len(dusts)+1)] for _ in range(len(dusts)+1)]
    for i, (x, y) in enumerate([robot]+dusts):
        visited = bfs(x, y)
        for j, (nx, ny) in enumerate(dusts):
            if nx == x and ny == y: continue
            if i == 0 and visited[nx][ny] == 0: flag = False
            distance[i][j+1] = visited[nx][ny]-1

    if flag:
        dusts = [i for i in range(1,len(dusts)+1)]
        cost = float("INF")
        for dust in permutations(dusts):
            pre_cost, start = 0, 0
            for d in dust:
                pre_cost += distance[start][d]
                start = d
            cost = min(cost,pre_cost)
        print(cost)
    else: print(-1)