#(1786) 찾기

import sys
import re

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
pi = [0 for _ in range(len(P))]

def fail(P):
    length, i = 0, 0
    for j in range(1,len(P)):
        while i > 0 and P[i] != P[j]:
            i = pi[i-1]
        if P[j] == P[i]:
            i += 1
            pi[j] = i

def KMP():
    i = 0
    index = []
    for j in range(len(T)):
        while i > 0 and T[j] != P[i]:
            i = pi[i-1]
        if T[j] == P[i]:
            if i == len(P)-1:
                index.append(j-len(P)+2)
                i = pi[i]
            else: i += 1
    return index
fail(P)
index = KMP()
print(len(index))
print(" ".join(map(str,index)))
