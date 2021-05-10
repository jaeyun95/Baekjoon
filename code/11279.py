#(11279) 최대 힙

import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(heap) == 0: print(0)
        else:
            out = heapq.heappop(heap)[1]
            print(out)
    else:
        heapq.heappush(heap,[-X,X])
