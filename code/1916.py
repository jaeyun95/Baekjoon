#(1916) 최소비용 구하기

import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus_list = [[] for _ in range(N+1)]
cost_dic = {key:float("INF") for key in range(1,N+1)}
for _ in range(M):
    a, b, cost = map(int,sys.stdin.readline().split())
    bus_list[a].append([b,cost])
start, end = map(int,sys.stdin.readline().split())

cost_dic[start] = 0
heap = []
heapq.heappush(heap,[cost_dic[start],start])
while heap:
    cost, node = heapq.heappop(heap)
    for next_node, next_cost in bus_list[node]:
        if cost_dic[next_node] > (next_cost + cost):
            cost_dic[next_node] = next_cost + cost
            heapq.heappush(heap,[cost_dic[next_node],next_node])

print(cost_dic[end])