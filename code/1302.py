#(1302) 베스트셀러

import sys

number = int(sys.stdin.readline())
sold_book = dict()
for _ in range(number):
    book = sys.stdin.readline().replace("\n","")
    sold_book[book] = sold_book.get(book,0)+1

sold_book = list(sold_book.items())
sold_book.sort(key = lambda x:(-x[1],x[0]))
print(sold_book[0][0])
