#(5052) 전화번호 목록

import sys

number = int(sys.stdin.readline())

for _ in range(number):
    call_num = int(sys.stdin.readline())
    tele_dir = []
    for _ in range(call_num):
        tele_dir.append(sys.stdin.readline().replace("\n",""))
    tele_dir.sort()
    check = 0
    for i in range(call_num-1):
        if tele_dir[i] in tele_dir[i+1][:len(tele_dir[i])]:
            print("NO")
            check = 1
            break
    if check == 0:
        print("YES")
