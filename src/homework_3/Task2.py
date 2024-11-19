from functools import reduce

product = 1
items = [1, 2, 3, 4]
result = reduce(lambda x, y:  x * y, items, product)
print("reduce:", result)