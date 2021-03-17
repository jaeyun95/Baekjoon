#(1181) 단어 정렬

import sys

number = int(input())
word_list = []
for _ in range(number):
    word_list.append(sys.stdin.readline().replace('\n',''))

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=lambda x:len(x))
for item in word_list:
    print(item)