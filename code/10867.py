#(10867) 중복 빼고 정렬하기

import sys

number = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
number_list = list(set(number_list))
number_list.sort()
print(*number_list)