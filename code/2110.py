#(2110) 공유기 설치

import sys

N, C = map(int, sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()
start, end = 1, max(house)-min(house)
result = 0
while start <= end:
    mid = (start + end)//2
    now = house[0]
    count = 1
    for h in house:
        if h >= now + mid:
            count += 1
            now = h
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)