#(1427) 소트인사이드

number_list = list(map(str,sorted(list(map(int,list(input()))),reverse=True)))
print(''.join(sorted(number_list,reverse=True)))