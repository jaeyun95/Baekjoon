#(1431) 시리얼 번호

import sys
import re

number = int(sys.stdin.readline())
serial_numbers = []
for _ in range(number):
    input_serial = sys.stdin.readline().replace('\n','')
    num_sum = sum(list(map(int, re.findall('\d',input_serial))))
    serial_numbers.append((input_serial,num_sum))

serial_numbers.sort(key=lambda x:(len(x[0]),x[1],x[0]))
for serial in serial_numbers:
    sys.stdout.write(serial[0]+"\n")


