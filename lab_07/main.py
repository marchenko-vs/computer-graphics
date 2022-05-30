import constants as const
import draw

from tkinter import *

window = Tk()
window.title("Лабораторная работа #7")
window.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}+0+0")
window.resizable(False, False)

canvas = Canvas(window, width=const.CANVAS_WIDTH, height=const.CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

lines = [[]]
rectangle = [-1, -1, -1, -1]

Label(text="Цвет отсекателя", font=("Calibri", 20, "bold")).place(width=445, height=25, y=5)

color_cut_var = IntVar()
color_cut_var.set(0)

Radiobutton(text="Черный", variable=color_cut_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=40)

Radiobutton(text="Красный", variable=color_cut_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=70)

Radiobutton(text="Синий", variable=color_cut_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=100)

Radiobutton(text="Зеленый", variable=color_cut_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=40)

Radiobutton(text="Желтый", variable=color_cut_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=70)

Radiobutton(text="Фиолетовый", variable=color_cut_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=170, height=25, x=260, y=100)

Label(text="Цвет отрезка", font=("Calibri", 20, "bold")).place(width=445, height=25, y=125)

color_line_var = IntVar()
color_line_var.set(3)

Radiobutton(text="Черный", variable=color_line_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=160)

Radiobutton(text="Красный", variable=color_line_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=190)

Radiobutton(text="Синий", variable=color_line_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=220)

Radiobutton(text="Зеленый", variable=color_line_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=160)

Radiobutton(text="Желтый", variable=color_line_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=190)

Radiobutton(text="Фиолетовый", variable=color_line_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=170, height=25, x=260, y=220)

Label(text="Цвет результата", font=("Calibri", 20, "bold")).place(width=445, height=25, x=0, y=245)

color_res_var = IntVar()
color_res_var.set(1)

Radiobutton(text="Черный", variable=color_res_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=280)

Radiobutton(text="Красный", variable=color_res_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=310)

Radiobutton(text="Синий", variable=color_res_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=340)

Radiobutton(text="Зеленый", variable=color_res_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=280)

Radiobutton(text="Желтый", variable=color_res_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=310)

Radiobutton(text="Фиолетовый", variable=color_res_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=170, height=20, x=260, y=340)

Label(text="Построение отрезка", font=("Calibri", 20, "bold")).place(width=445, height=25, x=0, y=365)

Label(text="Xн", font=("Calibri", 18)).place(width=35, height=20, x=40, y=400)
Label(text="Yн", font=("Calibri", 18)).place(width=35, height=20, x=40, y=435)
Label(text="Xк", font=("Calibri", 18)).place(width=35, height=20, x=240, y=400)
Label(text="Yк", font=("Calibri", 18)).place(width=35, height=20, x=240, y=435)

xb_entry = Entry(font=("Calibri", 18), justify='center')
xb_entry.place(width=100, height=30, x=90, y=400)

yb_entry = Entry(font=("Calibri", 18), justify='center')
yb_entry.place(width=100, height=30, x=90, y=435)

xe_entry = Entry(font=("Calibri", 18), justify='center')
xe_entry.place(width=100, height=30, x=290, y=400)

ye_entry = Entry(font=("Calibri", 18), justify='center')
ye_entry.place(width=100, height=30, x=290, y=435)

Button(text="Построить отрезок", font=("Calibri", 18),
       command=lambda: draw.add_line(lines, canvas, color_line_var,
                                     xb_entry, yb_entry, xe_entry, ye_entry)).place(width=370, height=50, x=40, y=470)

Label(text="Построение отсекателя", font=("Calibri", 20, "bold")).place(width=445, height=25, y=525)

Label(text="Xлв", font=("Calibri", 18)).place(width=35, height=20, x=40, y=560)
Label(text="Yлв", font=("Calibri", 18)).place(width=35, height=20, x=40, y=595)
Label(text="Xпн", font=("Calibri", 18)).place(width=35, height=20, x=240, y=560)
Label(text="Yпн", font=("Calibri", 18)).place(width=35, height=20, x=240, y=595)

x_top_left_entry = Entry(font=("Calibri", 18), justify='center')
x_top_left_entry.place(width=100, height=30, x=90, y=560)

y_top_left_entry = Entry(font=("Calibri", 18), justify='center')
y_top_left_entry.place(width=100, height=30, x=90, y=595)

x_lower_right_entry = Entry(font=("Calibri", 18), justify='center')
x_lower_right_entry.place(width=100, height=30, x=290, y=560)

y_lower_right_entry = Entry(font=("Calibri", 18), justify='center')
y_lower_right_entry.place(width=100, height=30, x=290, y=595)

Button(text="Построить отсекатель", font=("Calibri", 18),
       command=lambda: draw.draw_rectangle(rectangle, lines, canvas, color_cut_var,
                                           x_top_left_entry, y_top_left_entry,
                                           x_lower_right_entry, y_lower_right_entry)). \
    place(width=370, height=50, x=40, y=630)

Button(text="Добавить горизонтальные отрезки", font=("Calibri", 18),
       command=lambda: draw.add_horizontal_lines(rectangle, lines, canvas, color_line_var)). \
    place(width=370, height=50, x=40, y=740)

Button(text="Добавить вертикальные отрезки", font=("Calibri", 18),
       command=lambda: draw.add_vertical_lines(rectangle, lines, canvas, color_line_var)). \
    place(width=370, height=50, x=40, y=795)

Button(text="Отсечь", font=("Calibri", 18),
       command=lambda: draw.cut_off(rectangle, lines, canvas, color_res_var)). \
    place(width=370, height=50, x=40, y=850)

Button(text="Очистить экран", font=("Calibri", 18),
       command=lambda: draw.clear_canvas(canvas, lines, rectangle)). \
    place(width=370, height=50, x=40, y=905)

canvas.bind('<Button-1>',
            lambda event: draw.click_left(event))
canvas.bind('<Button-3>',
            lambda event: draw.click_right(event, lines, canvas, color_line_var))
canvas.bind('<B1-Motion>',
            lambda event: draw.click_left_motion(event, rectangle, lines, canvas, color_cut_var))

xb_entry.insert(0, '100')
yb_entry.insert(0, '200')

xe_entry.insert(0, '800')
ye_entry.insert(0, '500')

x_top_left_entry.insert(0, '200')
y_top_left_entry.insert(0, '100')

x_lower_right_entry.insert(0, '700')
y_lower_right_entry.insert(0, '600')

window.mainloop()
