#(11399) ATM

N = int(input())
time_list = list(map(int, input().split()))

sorted_list = sorted(time_list)
for i in range(1,len(sorted_list)):
    sorted_list[i] += sorted_list[i-1]

print(sum(sorted_list))