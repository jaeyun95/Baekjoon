#(1043) 거짓말

import sys

N, M = map(int,sys.stdin.readline().split())
true_people = set(map(int,sys.stdin.readline().split()[1:]))
party_people = []
possible = [True for _ in range(M)]
for _ in range(M):
    party_person = set(map(int,sys.stdin.readline().split()[1:]))
    party_people.append(party_person)

for _ in range(M):
    for i,p in enumerate(party_people):
        if true_people.intersection(p):
            possible[i] = False
            true_people = true_people.union(p)

print(possible.count(True))