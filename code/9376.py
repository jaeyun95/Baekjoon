#(9376) 탈옥

import sys
from collections import deque

moves = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited = [[-1 for _ in range(w+2)] for _ in range(h+2)]
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < h+2 and 0 <= ny < w+2 and visited[nx][ny] == -1:
                if prison[nx][ny] == "#":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                elif prison[nx][ny] in [".","$"]:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft([nx,ny])
    return visited

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    h, w = map(int,sys.stdin.readline().split())
    prison = []
    prisoner = []
    prison.append(['.']*(w+2))
    for _ in range(h):
        prison.append(['.']+list(sys.stdin.readline().rstrip())+['.'])
    prison.append(['.'] *(w+2))

    for i in range(h+2):
        for j in range(w+2):
            if prison[i][j] == "$":
                prisoner.append([i,j])
    a = bfs(prisoner[0][0],prisoner[0][1])
    b = bfs(prisoner[1][0],prisoner[1][1])
    open = bfs(0,0)
    result = float("INF")
    for x in range(h+2):
        for y in range(w+2):
            if prison[x][y] == "*": continue
            if a[x][y] != -1 and b[x][y] != -1 and open[x][y] != -1:
                door = a[x][y] + b[x][y] + open[x][y]
                if prison[x][y] == "#": door -= 2
                result = min(result,door)
    print(result)
