#(1449) 수리공 항승

import sys

num, tape = map(int, sys.stdin.readline().split())
holes = list(map(int, sys.stdin.readline().split()))
holes.sort()
count = 0
start = 0
for hole in holes:
    if start < hole:
        start = hole + tape - 1
        count += 1
print(count)