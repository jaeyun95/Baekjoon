#(2108) 통계학

import sys
from collections import Counter

number = int(input())
number_list = []
for _ in range(number):
    number_list.append(int(sys.stdin.readline()))

def mean(lst):
    return round(sum(lst)/len(lst))

def median(lst):
    return lst[len(lst)//2]

def mode(lst):
    num_dict = Counter(lst)
    num = num_dict.most_common()
    if len(num) > 1 and num[0][1] == num[1][1]:
        return num[1][0]
    else:
        return num[0][0]

def scope(lst):
    return lst[-1]-lst[0]

number_list.sort()
print(mean(number_list))
print(median(number_list))
print(mode(number_list))
print(scope(number_list))