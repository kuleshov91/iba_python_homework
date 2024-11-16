#3.	Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой
# равен сумме элементов, стоящих на том же месте в 1-й и 2-й таблицах.

import numpy

firstMatrix = numpy.array([[1, 3, 0], [3, 2, 6], [0, 6, 5]])
secondMatrix = numpy.array([[4, 7, 8], [1, 2, 6], [2, 9, 7]])
resultMatrix = firstMatrix + secondMatrix

print(resultMatrix)
