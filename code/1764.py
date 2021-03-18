#(1764) 듣보잡

import sys

nm = list(map(int, sys.stdin.readline().split()))
n_set = set()
m_set = set()
for _ in range(nm[0]):
    n_set.add(sys.stdin.readline().replace("\n",""))
for _ in range(nm[1]):
    m_set.add(sys.stdin.readline().replace("\n",""))

nm_list = list(n_set&m_set)
nm_list.sort()
sys.stdout.write(str(len(nm_list))+"\n")
for person in nm_list:
    sys.stdout.write(person+"\n")