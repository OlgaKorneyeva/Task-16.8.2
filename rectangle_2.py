from rectangle import Rectangle, Square, Circle

#далее создаем два прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

#далее создаем квадраты
square_1 = Square(5)
square_2 = Square(10)

#далее создаем круги
circle_1 = Circle(25)
circle_2 = Circle(35)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.area_r())
    else:
        print(figure.get_area())