#(11656) 접미사 배열

import sys

word = sys.stdin.readline().replace("\n","")
suffixs = []
for i in range(len(word)):
    suffixs.append(word[i:])
suffixs.sort()
for suffix in suffixs:
    sys.stdout.write(suffix+"\n")