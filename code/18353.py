#(18353) 병사 배치하기

import sys

N = int(sys.stdin.readline())
soldier = list(map(int, sys.stdin.readline().split()))
soldier.reverse()
cache = [1] * N

for n in range(1,N):
    for i in range(0,n):
        if soldier[i] < soldier[n]:
            cache[n] = max(cache[n],cache[i]+1)
print(N-max(cache))