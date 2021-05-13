#(18352) 특정 거리의 도시 찾기

import sys
from collections import deque

N, M, K, X = list(map(int, sys.stdin.readline().split()))
edges = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for _ in range(M):
    start, end = map(int,sys.stdin.readline().split())
    edges[start].append(end)

def bfs(edges, visited, start, k):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        start = queue.popleft()
        for end in edges[start]:
            if visited[end] == -1:
                visited[end] = visited[start] + 1
                queue.append(end)
    return visited

visited = bfs(edges,visited,X,K)
if K not in visited:
    print(-1)
else:
    for i in range(1,N+1):
        if visited[i] == K:
            print(i)
