#(11728) 배열 합치기

import sys

list_sizes = list(map(int, sys.stdin.readline().split()))
list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

concat_list = list_a+list_b
concat_list.sort()
print(*concat_list)