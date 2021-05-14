#(1806) 부분합

import sys

N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

sum_num = float("INF")
start, end, inter_num = 0, 0, 0

while True:
    if inter_num >= S:
        sum_num = min(sum_num,end-start)
        inter_num -= num_list[start]
        start += 1
    else:
        if end == N: break
        inter_num += num_list[end]
        end += 1

if sum_num == float("INF"): print(0)
else: print(sum_num)