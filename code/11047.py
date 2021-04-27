#(11047) 동전 0

import sys

N, K = map(int, sys.stdin.readline().split())
A = []
count = 0
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.reverse()
for value in A:
    count += (K//value)
    K %= value

print(count)