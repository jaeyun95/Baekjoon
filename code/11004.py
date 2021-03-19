#(11004) K번째 수

import sys

number = list(map(int, sys.stdin.readline().split()))
number_list = list(map(int, sys.stdin.readline().split()))

number_list.sort()
print(number_list[number[1]-1])