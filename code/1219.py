#(1219) 오민식의 고민

import sys

N, start, end, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append([e,c])

max_cost = list(map(int, sys.stdin.readline().split()))

def bfs(graph, city, en):
    visited = []
    queue = [city]
    while queue:
        now = queue.pop()
        if now == en:
            return True
        visited.append(now)
        for city, weight in graph[now]:
            if city not in visited:
                queue.append(city)
    return False

def bellman_ford(graph, st, en, max_cost):
    cost = [float("INF") for _ in range(N)]
    end_cost = []
    cost[st] = -max_cost[st]
    for i in range(N+1):
        for index in range(N):
            for city, weight in graph[index]:
                if cost[city] > cost[index] + weight - max_cost[city]:
                    cost[city] = cost[index] + weight - max_cost[city]
                    if i == N:
                        if bfs(graph,city,en):
                            return False
    return cost

result = bellman_ford(graph,start,end,max_cost)
if result:
    if result[end] == float("INF"): print("gg")
    else: print(-result[end])
else:
    print("Gee")