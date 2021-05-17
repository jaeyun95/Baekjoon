#(16954) 움직이는 미로 탈출

import sys
from collections import deque

maze = []
for _ in range(8):
    maze.append(list(sys.stdin.readline().rstrip()))

moves = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1],[0,0]]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        visited = [[False for _ in range(8)] for _ in range(8)]
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if [x,y] == [0,7]: return 1
            if maze[x][y] == '#': continue
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if maze[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
        maze.pop()
        maze.insert(0,['.', '.', '.', '.', '.', '.', '.', '.'])
    return 0

print(bfs(7,0))

