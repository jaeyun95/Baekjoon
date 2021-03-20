#(11652) 카드

import sys
from collections import Counter

number = int(sys.stdin.readline())
cards = []
for _ in range(number):
    cards.append(int(sys.stdin.readline()))

cards.sort()
cards_num = Counter(cards)
cards = list(cards_num.most_common())
print(cards[0][0])