#(1753) 최단경로

import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
root = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
INF = sys.maxsize
heap = []
distance = [INF] * (V+1)
for _ in range(E):
    start, end, value = map(int, sys.stdin.readline().split())
    graph[start].append([end,value])

def dijkstra(root):
    distance[root] = 0
    heapq.heappush(heap, (0,root))
    while heap:
        current_dis, current_node = heapq.heappop(heap)
        if distance[current_node] < current_dis: continue
        for next_node, dis in graph[current_node]:
            next_dis = dis + current_dis
            if distance[next_node] > next_dis:
                distance[next_node] = next_dis
                heapq.heappush(heap,(next_dis,next_node))

dijkstra(root)
for value in distance[1:]:
    print(value if value != INF else "INF")