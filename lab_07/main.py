from constants import *
from tkinter import *
from draw import clear_canvas, click_left, click_right, click_left_motion, \
    add_line, draw_rectangle, cut_off, add_vert_horiz_lines

window = Tk()
window.title("Лабораторная работа #7")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
window.resizable(False, False)

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

lines = [[]]
rectangle = [-1, -1, -1, -1]

Label(text="Цвет отсекателя", font=("Calibri", 18, "bold")).place(width=345, height=25, y=0)

color_cut_var = IntVar()
color_cut_var.set(0)

Radiobutton(text="Черный", variable=color_cut_var, value=0,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=25)

Radiobutton(text="Красный", variable=color_cut_var, value=1,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=45)

Radiobutton(text="Синий", variable=color_cut_var, value=2,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=65)

Radiobutton(text="Зеленый", variable=color_cut_var, value=3,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=25)

Radiobutton(text="Желтый", variable=color_cut_var, value=4,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=45)

Radiobutton(text="Фиолетовый", variable=color_cut_var, value=5,
            font=("Calibri", 16), anchor="w"). \
    place(width=140, height=20, x=180, y=65)

Label(text="Цвет отрезка", font=("Calibri", 18, "bold")).place(width=345, height=25, y=85)

color_line_var = IntVar()
color_line_var.set(3)

Radiobutton(text="Черный", variable=color_line_var, value=0,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=110)

Radiobutton(text="Красный", variable=color_line_var, value=1,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=130)

Radiobutton(text="Синий", variable=color_line_var, value=2,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=150)

Radiobutton(text="Зеленый", variable=color_line_var, value=3,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=110)

Radiobutton(text="Желтый", variable=color_line_var, value=4,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=130)

Radiobutton(text="Фиолетовый", variable=color_line_var, value=5,
            font=("Calibri", 16), anchor="w"). \
    place(width=140, height=20, x=180, y=150)

Label(text="Цвет результата", font=("Calibri", 18, "bold")).place(width=345, height=25, x=0, y=170)

color_res_var = IntVar()
color_res_var.set(1)

Radiobutton(text="Черный", variable=color_res_var, value=0,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=195)

Radiobutton(text="Красный", variable=color_res_var, value=1,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=215)

Radiobutton(text="Синий", variable=color_res_var, value=2,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=235)

Radiobutton(text="Зеленый", variable=color_res_var, value=3,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=195)

Radiobutton(text="Желтый", variable=color_res_var, value=4,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=215)

Radiobutton(text="Фиолетовый", variable=color_res_var, value=5,
            font=("Calibri", 16), anchor="w"). \
    place(width=140, height=20, x=180, y=235)

Label(text="Построение отрезка", font=("Calibri", 18, "bold")).place(width=345, height=25, x=0, y=255)

Label(text="Xн", font=("Calibri", 16)).place(width=20, height=20, x=50, y=285)
Label(text="Yн", font=("Calibri", 16)).place(width=20, height=20, x=125, y=285)
Label(text="Xк", font=("Calibri", 16)).place(width=20, height=20, x=200, y=285)
Label(text="Yк", font=("Calibri", 16)).place(width=20, height=20, x=275, y=285)

xb_entry = Entry(font=("Calibri", 16), justify='center')
xb_entry.place(width=70, height=30, x=25, y=310)

yb_entry = Entry(font=("Calibri", 16), justify='center')
yb_entry.place(width=70, height=30, x=100, y=310)

xe_entry = Entry(font=("Calibri", 16), justify='center')
xe_entry.place(width=70, height=30, x=175, y=310)

ye_entry = Entry(font=("Calibri", 16), justify='center')
ye_entry.place(width=75, height=30, x=250, y=310)

Button(text="Построить отрезок", font=("Calibri", 16),
       command=lambda: add_line(lines, canvas, color_line_var,
                                xb_entry, yb_entry, xe_entry, ye_entry)).place(width=300, height=35, x=25, y=345)

Label(text="Построение отсекателя", font=("Calibri", 18, "bold")).place(width=345,
                                                                        height=25, y=380)

Label(text="Xлв", font=("Calibri", 16)).place(width=35, height=20, x=45, y=410)
Label(text="Yлв", font=("Calibri", 16)).place(width=35, height=20, x=120, y=410)
Label(text="Xпн", font=("Calibri", 16)).place(width=35, height=20, x=195, y=410)
Label(text="Yпн", font=("Calibri", 16)).place(width=35, height=20, x=270, y=410)

x_top_left_entry = Entry(font=("Calibri", 16), justify='center')
x_top_left_entry.place(width=70, height=30, x=25, y=435)

y_top_left_entry = Entry(font=("Calibri", 16), justify='center')
y_top_left_entry.place(width=70, height=30, x=100, y=435)

x_lower_right_entry = Entry(font=("Calibri", 16), justify='center')
x_lower_right_entry.place(width=70, height=30, x=175, y=435)

y_lower_right_entry = Entry(font=("Calibri", 16), justify='center')
y_lower_right_entry.place(width=75, height=30, x=250, y=435)

Button(text="Построить отсекатель", font=("Calibri", 16),
       command=lambda: draw_rectangle(rectangle, lines, canvas, color_cut_var,
                                      x_top_left_entry, y_top_left_entry,
                                      x_lower_right_entry, y_lower_right_entry)). \
    place(width=300, height=35, x=25, y=470)

Button(text="Добавить горизонтальные\nи вертикальные отрезки", font=("Calibri", 16),
       command=lambda: add_vert_horiz_lines(rectangle, lines, canvas, color_line_var)). \
    place(width=300, height=50, x=25, y=510)

Button(text="Отсечь", font=("Calibri", 16),
       command=lambda: cut_off(rectangle, lines, canvas, color_res_var)). \
    place(width=300, height=35, x=25, y=565)

Button(text="Очистить экран", font=("Calibri", 16),
       command=lambda: clear_canvas(canvas, lines, rectangle)). \
    place(width=300, height=35, x=25, y=605)

canvas.bind('<Button-1>',
            lambda event: click_left(event))
canvas.bind('<Button-3>',
            lambda event: click_right(event, lines, canvas, color_line_var))
canvas.bind('<B1-Motion>',
            lambda event: click_left_motion(event, rectangle, lines, canvas, color_cut_var))

xb_entry.insert(0, '100')
yb_entry.insert(0, '200')

xe_entry.insert(0, '800')
ye_entry.insert(0, '500')

x_top_left_entry.insert(0, '200')
y_top_left_entry.insert(0, '100')

x_lower_right_entry.insert(0, '700')
y_lower_right_entry.insert(0, '600')

window.mainloop()
