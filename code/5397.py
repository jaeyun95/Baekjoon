#(5397) 키로거

import sys

L = int(sys.stdin.readline())
for _ in range(L):
    string = sys.stdin.readline().replace("\n","")
    left, right = [], []
    for chr in string:
        if chr == '<':
            if len(left) != 0:
                right.append(left.pop())
        elif chr == '>':
            if len(right) != 0:
                left.append(right.pop())
        elif chr == '-':
            if len(left) != 0:
                left.pop()
        else: left.append(chr)
    print(''.join(left+right[::-1]))
