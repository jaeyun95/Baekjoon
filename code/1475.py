#(1475) 방 번호

import sys
import math
N = sys.stdin.readline().rstrip()
count_list = [0 for _ in range(9)]

for num in N:
    if num == "6" or num == "9":
        count_list[6] += 0.5
        continue
    count_list[int(num)] += 1

print(math.ceil(max(count_list)))

