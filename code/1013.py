#(1013) Contact

import sys
import re

p = re.compile('(100+1+|01)+')
t = int(sys.stdin.readline())
for _ in range(t):
    signal = sys.stdin.readline().rstrip()
    if p.fullmatch(signal): print("YES")
    else: print("NO")
