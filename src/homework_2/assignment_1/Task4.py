# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.

from random import randint

numList = [randint(1, 10) for i in range(10)]
multiply = 1
max = 0

print("list before max element removing: ", numList)

for i in range(len(numList)):
    if i % 2 != 0:
        multiply *= numList[i]
    if numList[i] > max:
        max = numList[i]

numList.remove(max)

print("multiply of odd elements: ", multiply)
print("list after max element removing: ", numList)