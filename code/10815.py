#(10815) 숫자 카드

import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

def binary_search(lst, n, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if lst[mid] == n:
        return 1
    elif lst[mid] > n:
        return binary_search(lst, n, start, mid-1)
    else:
        return binary_search(lst, n, mid+1, end)

result_list = [0] * m
for i in range(m):
    result_list[i] = binary_search(n_list, m_list[i], 0, len(n_list)-1)

print(*result_list)

## using dictionary
'''
import sys

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

m_dict = {m_list[i] : 0 for i in range(m)}

for item in n_list:
    if item in m_dict.keys():
        m_dict[item] += 1

print(*m_dict.values())

'''