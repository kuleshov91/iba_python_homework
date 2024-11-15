count = 0

for i in range(3):
    num = int(input("Enter a number: \n"))
    if num < 0:
        count += 1

print("Quantity of negative numbers: ", count)