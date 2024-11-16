# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
# представленному в таблице ниже.
#------------------------------------------------------------------------------------------
#1	Удалить элемент с введенным номером a.
import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("Before delete: ", numList)

deleteIndex = int(input("Enter the index of the list to be deleted: \n"))
numList.pop(deleteIndex)

print("After delete: ", numList)