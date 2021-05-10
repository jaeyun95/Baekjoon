#(1904) 01타일

import sys

N = int(sys.stdin.readline())
cache = [0]*1000001
cache[1], cache[2] = 1, 2

for k in range(3,N+1):
    cache[k] = (cache[k-2]+cache[k-1])%15746
print(cache[N])
