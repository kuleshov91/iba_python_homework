# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.
from random import randint

numList = [randint(-10, 10) for i in range(12)]
max = -10
min = abs(numList[0])

for num in numList:
    if num % 2 != 0 and max < num:
        max = num
    if min > abs(num):
        min = abs(num)

print(numList)
print("max odd number: ", max)
print("min abs number: ", min)