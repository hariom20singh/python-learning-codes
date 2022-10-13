from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)
shape('triangle')


def draw_triangle(length=150):
    for i in range(3):
        forward(length)
        left(120)


for i in range(40):
    draw_triangle()
    right(10)

done()