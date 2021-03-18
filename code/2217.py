#(2217) 로프

import sys

number = int(input())
rope_list = []
for _ in range(number):
    rope_list.append(int(sys.stdin.readline()))

rope_list.sort(reverse=True)
weight = rope_list[0]
for i in range(1, number):
    count = i + 1
    if weight < rope_list[i] * count:
        weight = rope_list[i] * count
print(weight)
