#(9205) 맥주 마시면서 걸어가기

import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    cs = int(sys.stdin.readline())
    beer = 20
    position = []
    distance = [[False for _ in range(cs+2)] for _ in range(cs+2)]
    for _ in range(cs+2):
        position.append(list(map(int,sys.stdin.readline().split())))

    for i,pos1 in enumerate(position):
        for j,pos2 in enumerate(position):
            if i == j: continue
            if abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1]) <= beer*50:
                distance[i][j] = True

    for k in range(cs+2):
        for a in range(cs+2):
            for b in range(cs+2):
                if not distance[a][b]:
                    if distance[a][k] and distance[k][b]:
                        distance[a][b] = True
    if distance[0][-1]: print("happy")
    else: print("sad")
