#(2533) 사회망 서비스(SNS)

import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
network = [[] for _ in range(N+1)]
cache = [[0, 0] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int,sys.stdin.readline().split())
    network[start].append(end)
    network[end].append(start)

def dp(start):
    visited[start] = True
    cache[start][0] = 0
    cache[start][1] = 1
    for node in network[start]:
        if not visited[node]:
            dp(node)
            cache[start][0] += cache[node][1]
            cache[start][1] += min(cache[node][0],cache[node][1])

dp(1)
print(min(cache[1][0],cache[1][1]))