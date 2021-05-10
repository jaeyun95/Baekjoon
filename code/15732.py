#(15732) 도토리 숨기기

import sys

N, K, D = map(int, sys.stdin.readline().split())
rules = []
for _ in range(K):
    start, end, l = map(int,sys.stdin.readline().split())
    rules.append([start,end,l])

start, end = 1, N
ans = 0
while start <= end:
    mid = (end+start)//2
    count = 0
    for rule in rules:
        if rule[0] <= mid:
            count += ((min(mid,rule[1])-rule[0])//rule[2] + 1)
    if count >= D:
        ans = mid
        end = mid-1
    else:
        start = mid+1
print(ans)