#(1931) 회의실 배정

import sys

number = int(input())
meeting_list = []

for _ in range(number):
    meeting_list.append(tuple(map(int,sys.stdin.readline().split())))

meeting_list.sort(key=lambda x:(x[1],x[0]))

end = meeting_list[0][1]
count = 1
for item in meeting_list[1:]:
    if item[0] >= end:
        end = item[1]
        count += 1

print(count)