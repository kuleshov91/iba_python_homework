def square(x):
    return x ** 2

items = [1, 2, 3, 4, 5]
squared = list(map(square, items))
print("squared:", squared)