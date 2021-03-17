#(2751) 수 정렬하기2

import sys
number = int(input())
input_list = []

for i in range(number):
    input_list.append(int(sys.stdin.readline()))
    

## using python function
#for item in sorted(input_list):
#    ﻿sys.stdout.write﻿(str(item)+'\n')


## merge sort
'''
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    return merge(left_list,right_list)

def merge(left_list, right_list):
    sorted_list = []
    li = 0
    ri = 0
    while (li < len(left_list) and ri < len(right_list)):
        if left_list[li] < right_list[ri]:
            sorted_list.append(left_list[li])
            li += 1
        else:
            sorted_list.append(right_list[ri])
            ri += 1

    while(li < len(left_list)):
        sorted_list.append(left_list[li])
        li += 1
    while (ri < len(right_list)):
        sorted_list.append(right_list[ri])
        ri += 1
    return sorted_list

input_list = merge_sort(input_list)
'''
for item in sorted(input_list):
    ﻿sys.stdout.write﻿(str(item)+'\n')