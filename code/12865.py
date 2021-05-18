#(12865) 평범한 배낭

import sys

N, K = map(int, sys.stdin.readline().split())
items = []
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    items.append([W,V])

knapsack = [[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for w in range(1,K+1):
        if w >= items[i-1][0]:
            knapsack[i][w] = max(knapsack[i-1][w], knapsack[i-1][w-items[i-1][0]] + items[i-1][1])
        else:
            knapsack[i][w] = knapsack[i-1][w]

print(knapsack[-1][-1])