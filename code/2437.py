#(2437) 저울

import sys

number = int(sys.stdin.readline())
weight_list = list(map(int,sys.stdin.readline().split()))
weight_list.sort()
if weight_list[0] != 1: print(1)
else:
    no_weight = 1
    for weight in weight_list:
        if no_weight >= weight:
            no_weight += weight
        else:break
    print(no_weight)

