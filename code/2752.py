#(2752) 세수정렬

import sys

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
sys.stdout.write(str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2]))