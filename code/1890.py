#(1890) 점프

import sys

N = int(sys.stdin.readline())
maps = []
table = [[0 for _ in range(N)] for _ in range(N)]
table[0][0] = 1
for _ in range(N):
    maps.append(list(map(int,sys.stdin.readline().split())))

for x in range(N):
    for y in range(N):
        if table[x][y] != 0 and maps[x][y] != 0:
            if x + maps[x][y] < N:
                table[x + maps[x][y]][y] += table[x][y]
            if y + maps[x][y] < N:
                table[x][y + maps[x][y]] += table[x][y]
print(table[-1][-1])