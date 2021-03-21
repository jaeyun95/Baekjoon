#(1744) 수 묶기

import sys

number = int(sys.stdin.readline())
num_list = []
for _ in range(number):
    num_list.append(int(sys.stdin.readline()))
num_list.sort(reverse=True)
num_sum = 0
while len(num_list) > 0:
    if num_list[0] <= 0:
        num_list.sort()
    if len(num_list) == 1:
        num_sum += num_list.pop()
    else:
        if num_list[0] < (num_list[0] * num_list[1]):
            num_sum += (num_list.pop(0) * num_list.pop(0))
        else:
            num_sum += num_list.pop(0)
print(num_sum)