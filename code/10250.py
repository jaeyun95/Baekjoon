#(10250) ACM 호텔

import sys

N = int(sys.stdin.readline())
for _ in range(N):
    H, W, N = map(int, sys.stdin.readline().split())
    start = 0
    for w in range(1,W+1):
        for h in range(1,H+1):
            start += 1
            if start == N:
                if len(str(w)) == 1: print(str(h)+"0"+str(w))
                else:print(str(h)+str(w))
                break
