#(11650) 좌표 정렬하기

import sys

number = int(input())
position_list = []

for _ in range(number):
    position_list.append(tuple(map(int,sys.stdin.readline().split())))

position_list.sort(key=lambda x:(x[0],x[1]))

for position in position_list:
    sys.stdout.write(str(position[0])+" "+str(position[1])+"\n")