#(1026) 보물

import sys

number = int(input())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

index_list = [0] * number
for i, item in enumerate(sorted(b_list, reverse=True)):
    index_list[i] = b_list.index(item)

a_list.sort()
sum = 0
for i in range(number):
    sum += a_list[i]*b_list[index_list[i]]
print(sum)

"""
import sys

number = int(input())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

a_list.sort()
b_list.sort(reverse=True)
sum = 0
for i in range(number):
    sum += a_list[i]*b_list[i]
print(sum)

"""