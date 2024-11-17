# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

width = int(input("Enter width: "))
height = int(input("Enter height: "))
squareCount = 0
squareEdgesLength = []

def cutRectangle(width, height):
    global squareCount, squareEdgesLength

    if width == height:
        squareCount += 1
        squareEdgesLength.append(height)
        return

    if height < width:
        squareCount += 1
        squareEdgesLength.append(height)
        cutRectangle(width - height, height)
    elif height > width:
        squareCount += 1
        squareEdgesLength.append(width)
        cutRectangle(width, height - width)

cutRectangle(width, height)

print("square quantity: ", squareCount)
print("square edges length: ", squareEdgesLength)