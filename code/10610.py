#(10610) 30

import sys

num = list(sys.stdin.readline().replace("\n",""))
num.sort(reverse=True)
if int("".join(num))%3 != 0 or ('0' not in num):
    print("-1")
else:
    print("".join(num))