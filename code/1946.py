#(1946) 신입 사원

import sys

test_num = int(sys.stdin.readline())
for _ in range(test_num):
    test_case_num = int(sys.stdin.readline())
    people = []
    for _ in range(test_case_num):
        paper, interview = map(int,sys.stdin.readline().split())
        people.append([paper,interview])
    people.sort(key = lambda x:x[0])
    boundary = people[0][1]
    count = 1
    for i in range(1,test_case_num):
        if people[i][1] < boundary:
            count += 1
            boundary = people[i][1]
    print(count)