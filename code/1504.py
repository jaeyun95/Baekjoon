#(1504) 특정한 최단 경로

import sys
import heapq

def dijkstra(start):
    distance = {key: float("INF") for key in range(1, N + 1)}
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [distance[start], start])
    while heap:
        dis, node = heapq.heappop(heap)

        for next_node, next_dis in E_list[node]:
            if distance[next_node] > dis + next_dis:
                distance[next_node] = dis + next_dis
                heapq.heappush(heap, [distance[next_node], next_node])

    return distance

N, E = map(int,sys.stdin.readline().split())
E_list = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    E_list[a].append([b,c])
    E_list[b].append([a,c])

v1, v2 = map(int,sys.stdin.readline().split())

one_start = dijkstra(1)
v1_start = dijkstra(v1)
v2_start = dijkstra(v2)

cost = min(one_start[v1]+v1_start[v2]+v2_start[N],one_start[v2]+v2_start[v1]+v1_start[N])
if cost >= float("INF"): print(-1)
else: print(cost)