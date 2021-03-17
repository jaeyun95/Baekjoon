#(10989) 수 정렬하기3

import sys

number = int(input())
number_list = [0] * 10000

for _ in range(number):
    number_list[int(sys.stdin.readline())-1] += 1

for index, item in enumerate(number_list):
    if item != 0:
        for it in range(item):
            sys.stdout.write(str(index+1)+'\n')