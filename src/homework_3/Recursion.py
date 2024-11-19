# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

width = int(input("Enter width: "))
height = int(input("Enter height: "))
square_count = 0
square_edges_length = []

def cut_rectangle(width, height):
    global square_count, square_edges_length

    if width == height:
        square_count += 1
        square_edges_length.append(height)
        return

    if height < width:
        square_count += 1
        square_edges_length.append(height)
        cut_rectangle(width - height, height)
    elif height > width:
        square_count += 1
        square_edges_length.append(width)
        cut_rectangle(width, height - width)

cut_rectangle(width, height)

print("square quantity: ", square_count)
print("square edges length: ", square_edges_length)