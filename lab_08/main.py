import constants as const
import draw

from tkinter import *

window = Tk()
window.title("Лабораторная работа #8")
window.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}+0+0")
window.resizable(False, False)

canvas = Canvas(window, width=const.CANVAS_WIDTH, height=const.CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

lines = [[]]
clipping_window = []

Label(text="Цвет отсекателя", font=("Calibri", 20, "bold")).place(width=445, height=25, y=10)

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

Label(text="Цвет отрезка", font=("Calibri", 20, "bold")).place(width=445, height=25, y=140)

color_line_var = IntVar()
color_line_var.set(3)

Radiobutton(text="Черный", variable=color_line_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=170)

Radiobutton(text="Красный", variable=color_line_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=200)

Radiobutton(text="Синий", variable=color_line_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=230)

Radiobutton(text="Зеленый", variable=color_line_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=170)

Radiobutton(text="Желтый", variable=color_line_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=200)

Radiobutton(text="Фиолетовый", variable=color_line_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=170, height=25, x=260, y=230)

Label(text="Цвет результата", font=("Calibri", 20, "bold")).place(width=445, height=25, y=270)

color_res_var = IntVar()
color_res_var.set(1)

Radiobutton(text="Черный", variable=color_res_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=300)

Radiobutton(text="Красный", variable=color_res_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=330)

Radiobutton(text="Синий", variable=color_res_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=360)

Radiobutton(text="Зеленый", variable=color_res_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=300)

Radiobutton(text="Желтый", variable=color_res_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=330)

Radiobutton(text="Фиолетовый", variable=color_res_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=170, height=25, x=260, y=360)

Label(text="Построение отрезка", font=("Calibri", 20, "bold")).place(width=445, height=25, y=400)

Label(text="Xн\tYн\tXк\tYк", font=("Calibri", 18)).place(width=445, height=20, y=430)

xb_entry = Entry(font=("Calibri", 18), justify='center')
xb_entry.place(width=70, height=30, x=40, y=460)

yb_entry = Entry(font=("Calibri", 18), justify='center')
yb_entry.place(width=70, height=30, x=140, y=460)

xe_entry = Entry(font=("Calibri", 18), justify='center')
xe_entry.place(width=70, height=30, x=240, y=460)

ye_entry = Entry(font=("Calibri", 18), justify='center')
ye_entry.place(width=70, height=30, x=340, y=460)

Button(text="Построить отрезок", font=("Calibri", 18),
       command=lambda: draw.draw_line(lines, canvas, color_line_var,
                                      xb_entry, yb_entry, xe_entry, ye_entry)).place(width=370, height=50, x=40, y=495)

Label(text="Построение\nвершины отсекателя", font=("Calibri", 20, "bold")).place(width=445, y=550)

Label(text="X\t\tY", font=("Calibri", 18)).place(width=445, y=615)

x_cut_entry = Entry(font=("Calibri", 18), justify='center')
x_cut_entry.place(width=170, height=30, x=40, y=650)

y_cut_entry = Entry(font=("Calibri", 18), justify='center')
y_cut_entry.place(width=170, height=30, x=240, y=650)

Button(text="Построить вершину отсекателя", font=("Calibri", 18),
       command=lambda:
       draw.clipping_window_add_vertex(lines, clipping_window, canvas, color_cut_var, x_cut_entry, y_cut_entry)). \
    place(width=370, height=50, x=40, y=685)

Button(text="Замкнуть отсекатель", font=("Calibri", 18),
       command=lambda: draw.click_wheel(clipping_window, canvas, color_cut_var)). \
    place(width=370, height=50, x=40, y=740)

Button(text="Отсечь", font=("Calibri", 18),
       command=lambda: draw.clip(clipping_window, lines, canvas, color_cut_var, color_res_var)). \
    place(width=370, height=50, x=40, y=850)

Button(text="Очистить экран", font=("Calibri", 18),
       command=lambda: draw.clear_canvas(canvas, lines, clipping_window)).place(width=370, height=50, x=40, y=905)

canvas.bind('<Button-1>',
            lambda event: draw.click_right(event, lines, clipping_window, canvas, color_cut_var))
canvas.bind('<Button-2>',
            lambda event: draw.click_wheel(clipping_window, canvas, color_cut_var))
canvas.bind('<Button-3>',
            lambda event: draw.click_left(event, lines, canvas, color_line_var))

xb_entry.insert(0, '100')
yb_entry.insert(0, '200')

xe_entry.insert(0, '800')
ye_entry.insert(0, '500')

x_cut_entry.insert(0, '200')
y_cut_entry.insert(0, '100')

window.mainloop()
