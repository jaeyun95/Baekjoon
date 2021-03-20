#(8979) 올림픽

import sys

number = list(map(int,sys.stdin.readline().split()))
nation_list = []
for _ in range(number[0]):
    nation_list.append(list(map(int, sys.stdin.readline().split())))
nation_list.sort(key = lambda x:(x[1],x[2],x[3]),reverse=True)

count = 1
for i in range(number[0]):
    if nation_list[i][0] == number[1]:
        standard = nation_list[i]

for i in range(number[0]):
    if nation_list[i][1:] == standard[1:]:
        print(count)
        break
    count += 1