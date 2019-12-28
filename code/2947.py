#(2947) 나무 조각

input_list = list(map(int,input().split()))
for i in range(len(input_list)-1):
    for j in range(len(input_list)-i-1):
        if input_list[j] > input_list[j+1]:
            input_list[j], input_list[j+1]=input_list[j+1], input_list[j]
            print(*input_list)