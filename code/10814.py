#(10814) 나이순 정렬

import sys

number = int(input())
information_list = []
index = 0
for _ in range(number):
    pre_information = sys.stdin.readline().split()
    information_list.append((int(pre_information[0]),pre_information[1],index))
    index += 1

information_list.sort(key=lambda x:(x[0],x[2]))

for infor in information_list:
    sys.stdout.write(str(infor[0])+" "+str(infor[1])+"\n")