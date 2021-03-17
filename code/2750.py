#(2750) 수 정렬하기

number = int(input())
input_list = []

for _ in range(number):
    input_list.append(int(input()))

## using python function
#input_list = sorted(input_list)

## bubble sort
'''
for i in range(len(input_list)-1):
    for j in range(len(input_list)-i-1):
        if input_list[j] > input_list[j+1]:
            input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
'''

## selection sort
'''
for i in range(len(input_list)):
    index = i
    for j in range(i+1,len(input_list)):
        if input_list[index] > input_list[j]:
            index = j
    input_list[i], input_list[index] = input_list[index], input_list[i]
'''

## insertion sort
'''
for i in range(1,len(input_list)):
    for j in range(i,0,-1):
        if input_list[j] < input_list[j-1]:
            input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
'''

## merge sort
'''
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    return merge(left_list,right_list)

def merge(left_list, right_list):
    sorted_list = []
    li = 0
    ri = 0
    while (li < len(left_list) and ri < len(right_list)):
        if left_list[li] < right_list[ri]:
            sorted_list.append(left_list[li])
            li += 1
        else:
            sorted_list.append(right_list[ri])
            ri += 1

    while(li < len(left_list)):
        sorted_list.append(left_list[li])
        li += 1
    while (ri < len(right_list)):
        sorted_list.append(right_list[ri])
        ri += 1
    return sorted_list

input_list = merge_sort(input_list)
'''

## heap sort
'''
def heapify(lst, index, size):
    parent = index
    child = 2 * index + 1
    if child < size and lst[child] > lst[parent]:
        parent = child
    if (child + 1) < size and lst[(child + 1)] > lst[parent]:
        parent = (child + 1)
    if parent != index:
        lst[parent], lst[index] = lst[index], lst[parent]
        heapify(lst, parent, size)

def heap_sort(lst):
    for i in range(len(lst)//2-1,-1,-1):
        heapify(lst, i, len(lst))
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i)
    return lst

input_list = heap_sort(input_list)
'''

## quick sort
'''
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left, right = [], []
    for item in lst[1:]:
        if item < pivot: left.append(item)
        else: right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)

input_list = quick_sort(input_list)
'''

## counting sort
'''
def counting_sort(lst, K):
    count_lst = [0] * K
    sorted_lst = [0] * len(lst)

    for item in lst:
        count_lst[item] += 1

    for count in range(1,K):
        count_lst[count] += count_lst[count-1]

    for index in range(len(lst)):
        sorted_lst[count_lst[lst[index]]-1] = lst[index]
        count_lst[lst[index]] -= 1
    return sorted_lst

input_list = counting_sort(input_list,max(input_list)+1)
'''

for item in input_list:
    print(item)

