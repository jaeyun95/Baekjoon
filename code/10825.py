#(10825) 국영수

import sys

number = int(sys.stdin.readline())
informations = []
for _ in range(number):
    information = sys.stdin.readline().split()
    informations.append((information[0],int(information[1]),int(information[2]),int(information[3])))
informations.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))
for person in informations:
    sys.stdout.write(person[0]+"\n")