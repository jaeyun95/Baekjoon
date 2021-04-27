#(8980) 택배

import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
box_list = []
for _ in range(M):
    box_list.append(list(map(int,sys.stdin.readline().split())))

box_list.sort(key=lambda x:x[1])
truck_list = [C]*(N+1)
count = 0
for box in box_list:
    minTruck = C
    for i in range(box[0],box[1]):
        minTruck = min(truck_list[i], minTruck)
    count += min(minTruck,box[2])
    for i in range(box[0],box[1]):
        truck_list[i] -= min(minTruck,box[2])
print(count)