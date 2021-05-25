#(10830) 행렬 제곱

import sys

N, B = map(int, sys.stdin.readline().split())
matrix = []
for n in range(N):
    row = list(map(lambda x: int(x)%1000, sys.stdin.readline().split()))
    matrix.append(row)

def matmul(matrix1, matrix2):
    new_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_matrix[i][j] += sum([matrix1[i][k]%1000*matrix2[k][j]%1000 for k in range(N)])%1000
    return new_matrix


def split_num(num):
    if num == 1: return matrix
    new_matrix = split_num(num//2)
    new_matrix = matmul(new_matrix,new_matrix)
    if num % 2 == 1:
        new_matrix = matmul(new_matrix,matrix)
    return new_matrix

for num in split_num(B):
    print(" ".join(map(str,num)))