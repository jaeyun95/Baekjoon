#(8983) 사냥꾼

import sys

M, N, L = map(int, sys.stdin.readline().split())
M_location = list(map(int, sys.stdin.readline().split()))
M_location.sort()
N_location = []
count = 0
for _ in range(N):
    N_location.append(list(map(int,sys.stdin.readline().split())))

N_location.sort(key=lambda x:x[0])

for n_loc in N_location:
    start = 0
    end = len(M_location) - 1
    while start < end:
        mid = (start + end) // 2
        if M_location[mid] < n_loc[0]: start = mid + 1
        else: end = mid
    if abs(M_location[end] - n_loc[0]) + n_loc[1] <= L or abs(M_location[end - 1] - n_loc[0]) + n_loc[1] <= L:
        count += 1
print(count)

