from constants import *
from draw import clear_canvas, click_left, click_right, click_centre, \
    add_line, add_vertex_figure, cut_off
from tkinter import *

window = Tk()
window.title("Лабораторная работа #8")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
window.resizable(False, False)

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

lines = [[]]
cutter_figure = []

Label(text="Цвет отсекателя", font=("Calibri", 18, "bold")).place(width=345, height=25, y=0)

color_cut_var = IntVar()
color_cut_var.set(0)

Radiobutton(text="Черный", variable=color_cut_var, value=0,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=30)

Radiobutton(text="Красный", variable=color_cut_var, value=1,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=50)

Radiobutton(text="Синий", variable=color_cut_var, value=2,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=70)

Radiobutton(text="Зеленый", variable=color_cut_var, value=3,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=30)

Radiobutton(text="Желтый", variable=color_cut_var, value=4,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=50)

Radiobutton(text="Фиолетовый", variable=color_cut_var, value=5,
            font=("Calibri", 16), anchor="w"). \
    place(width=140, height=20, x=180, y=70)

Label(text="Цвет отрезка", font=("Calibri", 18, "bold")).place(width=345, height=25, y=95)

color_line_var = IntVar()
color_line_var.set(3)

Radiobutton(text="Черный", variable=color_line_var, value=0,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=125)

Radiobutton(text="Красный", variable=color_line_var, value=1,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=145)

Radiobutton(text="Синий", variable=color_line_var, value=2,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=165)

Radiobutton(text="Зеленый", variable=color_line_var, value=3,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=125)

Radiobutton(text="Желтый", variable=color_line_var, value=4,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=145)

Radiobutton(text="Фиолетовый", variable=color_line_var, value=5,
            font=("Calibri", 16), anchor="w"). \
    place(width=140, height=20, x=180, y=165)

Label(text="Цвет результата", font=("Calibri", 18, "bold")).place(width=345, height=25, y=190)

color_res_var = IntVar()
color_res_var.set(1)

Radiobutton(text="Черный", variable=color_res_var, value=0,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=220)

Radiobutton(text="Красный", variable=color_res_var, value=1,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=240)

Radiobutton(text="Синий", variable=color_res_var, value=2,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=20, y=260)

Radiobutton(text="Зеленый", variable=color_res_var, value=3,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=220)

Radiobutton(text="Желтый", variable=color_res_var, value=4,
            font=("Calibri", 16), anchor="w"). \
    place(width=120, height=20, x=180, y=240)

Radiobutton(text="Фиолетовый", variable=color_res_var, value=5,
            font=("Calibri", 16), anchor="w"). \
    place(width=140, height=20, x=180, y=260)

Label(text="Построение отрезка", font=("Calibri", 18, "bold")).place(width=345, height=25, y=285)

Label(text="Xн\tYн\tXк\tYк", font=("Calibri", 16)).place(width=345, height=20, y=310)

xb_entry = Entry(font=("Calibri", 16), justify='center')
xb_entry.place(width=67, height=30, x=25, y=335)

yb_entry = Entry(font=("Calibri", 16), justify='center')
yb_entry.place(width=67, height=30, x=90, y=335)

xe_entry = Entry(font=("Calibri", 16), justify='center')
xe_entry.place(width=67, height=30, x=155, y=335)

ye_entry = Entry(font=("Calibri", 16), justify='center')
ye_entry.place(width=67, height=30, x=220, y=335)

Button(text="Построить отрезок", font=("Calibri", 16),
       command=lambda: add_line(lines, canvas, color_line_var,
                                xb_entry, yb_entry, xe_entry, ye_entry)). \
    place(width=300, height=35, x=25, y=370)

Label(text="Построение\nвершины отсекателя", font=("Calibri", 18, "bold")) \
    .place(width=345, y=405)

Label(text="X\t\tY", font=("Calibri", 16)).place(width=345, y=460)

x_cut_entry = Entry(font=("Calibri", 16), justify='center')
x_cut_entry.place(width=134, height=30, x=25, y=490)

y_cut_entry = Entry(font=("Calibri", 16), justify='center')
y_cut_entry.place(width=134, height=30, x=160, y=490)

Button(text="Построить вершину отсекателя", font=("Calibri", 16),
       command=lambda:
       add_vertex_figure(lines, cutter_figure, canvas, color_cut_var, x_cut_entry, y_cut_entry)). \
    place(width=300, height=35, x=25, y=525)

Button(text="Замкнуть отсекатель", font=("Calibri", 16),
       command=lambda: click_centre(cutter_figure, canvas, color_cut_var)). \
    place(width=300, height=35, x=25, y=565)

Button(text="Отсечь", font=("Calibri", 16),
       command=lambda: cut_off(cutter_figure, lines, canvas, color_cut_var, color_res_var)). \
    place(width=300, height=35, x=25, y=605)

Button(text="Очистить экран", font=("Calibri", 16),
       command=lambda: clear_canvas(canvas, lines, cutter_figure)). \
    place(width=300, height=35, x=25, y=645)

canvas.bind('<Button-1>',
            lambda event: click_left(event, lines, canvas, color_line_var))
canvas.bind('<Button-2>',
            lambda event: click_centre(cutter_figure, canvas, color_cut_var))
canvas.bind('<Button-3>',
            lambda event: click_right(event, lines, cutter_figure, canvas, color_cut_var))

xb_entry.insert(0, '100')
yb_entry.insert(0, '200')

xe_entry.insert(0, '800')
ye_entry.insert(0, '500')

x_cut_entry.insert(0, '200')
y_cut_entry.insert(0, '100')

window.mainloop()
