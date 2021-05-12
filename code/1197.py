#(1197) 최소 스패닝 트리

import sys
from collections import deque

V, E = map(int, sys.stdin.readline().split())
parent = [0] * (V+1)
graph = []
for i in range(1,V+1):
    parent[i] = i
for _ in range(E):
    graph.append(list(map(int, sys.stdin.readline().split())))

def is_parent(parent,x):
    if parent[x] != x:
        parent[x] = is_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = is_parent(parent,a)
    b = is_parent(parent,b)
    if a < b: parent[b] = a
    else: parent[a] = b

graph.sort(key=lambda x:x[2])
result = 0
for a, b, cost in graph:
    if is_parent(parent,a) != is_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)