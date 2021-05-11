#(10282) 해킹

import sys
import heapq

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n, d, c = map(int,sys.stdin.readline().split())
    computer_list = [[] for _ in range(n+1)]
    dependence = {key:float('INF') for key in range(1,n+1)}
    for _ in range(d):
        a, b, s = map(int,sys.stdin.readline().split())
        computer_list[b].append([a,s])

    dependence[c] = 0
    heap = []
    heapq.heappush(heap,[dependence[c],c])
    while heap:
        dis, computer = heapq.heappop(heap)
        for b, s in computer_list[computer]:
            if dependence[b] > dis + s:
                dependence[b] = dis+s
                heapq.heappush(heap,[dependence[b],b])
    count = 0
    hour = 0
    for k, v in dependence.items():
        if v != float("INF"):
            hour = max(hour,v)
            count += 1

    print(count,hour)