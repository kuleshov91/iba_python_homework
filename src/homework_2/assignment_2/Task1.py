# 1. В матрице найти номер строки, сумма чисел в которой максимальна.

matrix = [[-3, 0, 2], [5, 7, -1], [3, -8, 9], [4, 2, 7]]

sum = 0
max = 0
maxRow = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
    if sum > max:
        max = sum
        maxRow = i

print(matrix)
print("number of the max row: ", maxRow)
