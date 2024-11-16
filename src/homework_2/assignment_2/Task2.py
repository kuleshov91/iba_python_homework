#2.	Симметричная матрица.
# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.

symmetricMatrix = [[1, 3, 0], [3, 2, 6], [0, 6, 5]]
notSymmetricMatrix = [[4, 7, 8], [1, 2, 6], [2, 9, 7]]

def isSymmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == matrix[j][i]:
                continue
            else:
                return False    
    return True

print(isSymmetric(symmetricMatrix))
print(isSymmetric(notSymmetricMatrix))