#(13460) 구슬 탈출 2

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = []
moves = [[-1,0],[1,0],[0,-1],[0,1]]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    line = list(sys.stdin.readline().rstrip())
    maze.append(line)
    if "R" in line: red = [i,line.index("R")]
    if "B" in line: blue = [i,line.index("B")]

def new_location(maze,start,move):
    x = start[0]
    y = start[1]
    while True:
        nx = x + move[0]
        ny = y + move[1]
        if maze[nx][ny] == "#": return [x,y]
        if maze[nx][ny] == "O": return [nx,ny]
        if maze[nx][ny] != "#":
            x, y = nx, ny

def bfs(maze,visited,red,blue):
    visited[red[0]][red[1]][blue[0]][blue[1]] = True
    queue = deque()
    queue.append([red, blue, 1])
    while queue:
        red, blue, count = queue.popleft()
        for move in moves:
            new_R = new_location(maze,red,move)
            new_B = new_location(maze, blue, move)
            if maze[new_B[0]][new_B[1]] == "O": continue
            if maze[new_R[0]][new_R[1]] == "O": return count
            if new_R == new_B:
                if (abs(red[0]-new_R[0])+abs(red[1]-new_R[1])) > (abs(blue[0]-new_B[0])+abs(blue[1]-new_B[1])):
                    new_R[0] -= move[0]
                    new_R[1] -= move[1]
                else:
                    new_B[0] -= move[0]
                    new_B[1] -= move[1]
            if not visited[new_R[0]][new_R[1]][new_B[0]][new_B[1]]:
                visited[new_R[0]][new_R[1]][new_B[0]][new_B[1]] = True
                queue.append([new_R,new_B,count+1])
        if count > 10:
            return -1
    return -1
print(bfs(maze,visited,red,blue))
