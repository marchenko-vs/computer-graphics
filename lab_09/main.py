import draw

from constants import *
from tkinter import Tk, Radiobutton, Canvas, Label, Entry, Button, DISABLED, IntVar

main_window = Tk()
main_window.title("Лабораторная работа #9")
main_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
main_window.resizable(False, False)

canvas = Canvas(main_window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

figure = list()
clipper = list()

Label(text="Цвет отсекателя", font=("Calibri", 20, "bold")).place(width=445)

color_clipper_var = IntVar()
color_clipper_var.set(0)

Radiobutton(text="Черный", variable=color_clipper_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=40)

Radiobutton(text="Красный", variable=color_clipper_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=70)

Radiobutton(text="Синий", variable=color_clipper_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=100)

Radiobutton(text="Зеленый", variable=color_clipper_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=40)

Radiobutton(text="Желтый", variable=color_clipper_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=70)

Radiobutton(text="Фиолетовый", variable=color_clipper_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=160, height=25, x=260, y=100)

Label(text="Цвет фигуры", font=("Calibri", 20, "bold")).place(width=445, y=130)

color_figure_var = IntVar()
color_figure_var.set(3)

Radiobutton(text="Черный", variable=color_figure_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=170)

Radiobutton(text="Красный", variable=color_figure_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=200)

Radiobutton(text="Синий", variable=color_figure_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=230)

Radiobutton(text="Зеленый", variable=color_figure_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=170)

Radiobutton(text="Желтый", variable=color_figure_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=200)

Radiobutton(text="Фиолетовый", variable=color_figure_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=160, height=25, x=260, y=230)

Label(text="Цвет результата", font=("Calibri", 20, "bold")).place(width=445, y=260)

color_result_var = IntVar()
color_result_var.set(1)

Radiobutton(text="Черный", variable=color_result_var, value=0,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=300)

Radiobutton(text="Красный", variable=color_result_var, value=1,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=330)

Radiobutton(text="Синий", variable=color_result_var, value=2,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=360)

Radiobutton(text="Зеленый", variable=color_result_var, value=3,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=300)

Radiobutton(text="Желтый", variable=color_result_var, value=4,
            font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=330)

Radiobutton(text="Фиолетовый", variable=color_result_var, value=5,
            font=("Calibri", 18), anchor="w").place(width=160, height=25, x=260, y=360)

Label(text="Построение вершин фигуры", font=("Calibri", 20, "bold")).place(width=445, y=390)

Label(text="X", font=("Calibri", 18)).place(x=115, y=425)
Label(text="Y", font=("Calibri", 18)).place(x=315, y=425)

entry_figure_x = Entry(font=("Calibri", 18), justify='center')
entry_figure_x.place(width=170, height=30, x=40, y=460)

entry_figure_y = Entry(font=("Calibri", 18), justify='center')
entry_figure_y.place(width=170, height=30, x=240, y=460)

Button(text="Построить вершину", font=("Calibri", 18),
       command=lambda:
       draw.add_vertex(clipper, figure, canvas, color_figure_var, color_clipper_var, entry_figure_x, entry_figure_y)). \
    place(width=370, height=50, x=40, y=495)

Button(text="Замкнуть фигуру", font=("Calibri", 18),
       command=lambda: draw.close_figure(figure, canvas, color_figure_var, info_name="Фигура должна")). \
    place(width=370, height=50, x=40, y=550)

Label(text="Построение вершин отсекателя", font=("Calibri", 20, "bold")).place(width=445, y=610)

Label(text="X", font=("Calibri", 18)).place(x=115, y=645)
Label(text="Y", font=("Calibri", 18)).place(x=315, y=645)

entry_clipper_x = Entry(font=("Calibri", 18), justify='center')
entry_clipper_x.place(width=170, height=30, x=40, y=680)

entry_clipper_y = Entry(font=("Calibri", 18), justify='center')
entry_clipper_y.place(width=170, height=30, x=240, y=680)

Button(text="Построить вершину", font=("Calibri", 18),
       command=lambda:
       draw.add_vertex(figure, clipper, canvas, color_clipper_var, color_figure_var, entry_clipper_x, entry_clipper_y)). \
    place(width=370, height=50, x=40, y=715)

Button(text="Замкнуть отсекатель", font=("Calibri", 18),
       command=lambda: draw.close_figure(clipper, canvas, color_clipper_var, info_name="Отсекатель должен")). \
    place(width=370, height=50, x=40, y=770)

Button(text="Отсечь", font=("Calibri", 18),
       command=lambda: draw.clip(clipper, figure, canvas, color_result_var)). \
    place(width=370, height=50, x=40, y=880)

Button(text="Очистить экран", font=("Calibri", 18),
       command=lambda: draw.clear_canvas(canvas, figure, clipper)). \
    place(width=370, height=50, x=40, y=935)

canvas.bind('<Button-1>',
            lambda event: draw.click_left(event, figure, clipper, canvas, color_clipper_var, color_figure_var))
canvas.bind('<Button-3>',
            lambda event: draw.click_right(event, clipper, figure, canvas, color_figure_var, color_clipper_var))

entry_figure_x.insert(0, '100')
entry_figure_y.insert(0, '200')

entry_clipper_x.insert(0, '200')
entry_clipper_y.insert(0, '100')

main_window.mainloop()
