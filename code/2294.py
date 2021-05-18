#(2294) 동전 2

import sys

n, k = map(int,sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

coin = list(set(coin))
cache = [float("INF") for _ in range(k+1)]
cache[0] = 0
for c in coin:
    for value in range(c,k+1):
        if cache[value-c] != float("INF"):
            cache[value] = min(cache[value],cache[value-c]+1)

if cache[-1] != float("INF"): print(cache[-1])
else: print(-1)