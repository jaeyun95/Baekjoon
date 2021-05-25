#(1241) 머리 톡톡

import sys

N = int(sys.stdin.readline())
circle, result = [], [0 for _ in range(N)]
for i in range(N):
    circle.append(int(sys.stdin.readline()))

matrix = [0 for _ in range(max(circle)+1)]
for num in circle:
    matrix[num] += 1

for i in range(N):
    k = 1
    while k*k <= (circle[i]):
        if circle[i] % k == 0:
            if k*k != circle[i]:
                result[i] += matrix[k] + matrix[circle[i]//k]
            else:
                result[i] += matrix[k]
        k += 1

for r in result:
    print(r-1)
