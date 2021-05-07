#(2839) 설탕배달

import sys

N = int(sys.stdin.readline())
cache = [float("INF")] * (N+1)
cache[0] = 0
sugar_list = [3,5]

for n in sugar_list:
    for m in range(n, N+1):
        if cache[m-n] != float("INF"):
            cache[m] = min(cache[m], cache[m-n]+1)
if cache[N] == float("INF"): print(-1)
else: print(cache[N])
