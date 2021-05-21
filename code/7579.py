#(7579) 앱

import sys

N, M = map(int,sys.stdin.readline().split())
bites = list(map(int,sys.stdin.readline().split(" ")))
cost = list(map(int,sys.stdin.readline().split(" ")))
cost_sum = [[0 for _ in range(sum(cost)+1)] for _ in range(N+1)]
answer = sum(cost)

for a in range(1,N+1):
    for b in range(1,len(cost_sum[0])):
        if b >= cost[a-1]:
            cost_sum[a][b] = max(cost_sum[a-1][b],cost_sum[a-1][b-cost[a-1]]+bites[a-1])
        else: cost_sum[a][b] = cost_sum[a-1][b]
        if cost_sum[a][b] >= M: answer = min(answer,b)

print(answer)

