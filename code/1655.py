#(1655) 가운데를 말해요

import sys
import heapq

N = int(sys.stdin.readline())
left_heap = []
right_heap = []
mid_list = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap,(-number,number))
    else:
        heapq.heappush(right_heap,(number,number))
    if len(left_heap) != 0 and len(right_heap) != 0 and left_heap[0][1] > right_heap[0][1]:
            left_number = heapq.heappop(left_heap)[1]
            right_number = heapq.heappop(right_heap)[1]
            heapq.heappush(left_heap,(-right_number,right_number))
            heapq.heappush(right_heap, (left_number, left_number))
    mid_list.append(left_heap[0][1])

for mid in mid_list:
    sys.stdout.write(str(mid)+"\n")