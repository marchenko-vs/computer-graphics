from constants import *
from draw import *
from tkinter import *


window = Tk()
window.title("Лабораторная работа #5")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
window.resizable(False, False)

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

figures = [[[]]]

p_min = [CANVAS_WIDTH, CANVAS_HEIGHT]
p_max = [0, 0]

Label(text="Цвет закраски", font=("Calibri", 18, "bold")).place(width=345, x=0, y=0)

color_var = IntVar()
color_var.set(1)

Radiobutton(text="Черный", variable=color_var, value=0,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=20, y=40)

Radiobutton(text="Красный", variable=color_var, value=1,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=20, y=60)

Radiobutton(text="Синий", variable=color_var, value=2,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=20, y=80)

Radiobutton(text="Зеленый", variable=color_var, value=3,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=180, y=40)

Radiobutton(text="Желтый", variable=color_var, value=4,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=180, y=60)

Radiobutton(text="Фиолетовый", variable=color_var, value=5,
            font=("Calibri", 16), anchor="w").place(width=150, height=20, x=180, y=80)

Label(text="Режим закраски", font=("Calibri", 18, "bold")).place(width=345, height=25, x=0, y=100)

mode_var = BooleanVar()
mode_var.set(True)

Radiobutton(text="Без задержки", variable=mode_var, value=0,
            font=("Calibri", 16), anchor="w").place(width=150, x=20, y=125)

Radiobutton(text="С задержкой", variable=mode_var, value=1,
            font=("Calibri", 16), anchor="w").place(width=150, x=180, y=125)

Label(text="Добавление точки", font=("Calibri", 18, "bold")).place(width=345, height=30, x=0, y=160)

Label(text="X", font=("Calibri", 16)).place(height=20, x=85, y=190)

Label(text="Y", font=("Calibri", 16)).place(height=20, x=245, y=190)

x_entry = Entry(font=("Calibri", 16), justify='center')
x_entry.place(width=125, height=30, x=30, y=215)

y_entry = Entry(font=("Calibri", 16), justify='center')
y_entry.place(width=125, height=30, x=190, y=215)

Button(text="Построить точку", font=("Calibri", 17),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda: draw_point(figures, img, color_var, x_entry, y_entry,
                                  p_min, p_max, points_listbox)).place(width=285, height=36, x=30, y=253)

points_listbox = Listbox(font=("Calibri", 16))
points_listbox.place(width=285, height=130, x=30, y=295)

Label(text="Построение с помощью мыши",
      font=("Calibri", 18, "bold")).place(width=345, height=30, x=0, y=430)

Label(text="Левая кнопка - добавить точку",
      font=("Calibri", 16)).place(width=345, height=25, x=0, y=460)

Label(text="Правая кнопка - замкнуть фигуру",
      font=("Calibri", 16)).place(width=345, height=25, x=0, y=490)

Label(text="Время закраски:", font=("Calibri", 16)).place(width=150, height=30, x=20, y=520)

time_entry = Entry(font=("Calibri", 16), justify='center')
time_entry.place(width=135, height=30, x=180, y=520)

Button(text="Выполнить закраску", font=("Calibri", 17),
       highlightbackground="#d1d1e0", highlightthickness=30,
       command=lambda: fill_figure(figures, img, canvas, color_var, p_min, p_max, mode_var, time_entry)). \
    place(width=285, height=36, x=30, y=560)

Button(text="Очистить экран", font=("Calibri", 17),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda: clear_canvas(img, canvas, figures, p_min, p_max,
                                    time_entry, points_listbox)).place(width=285, height=36, x=30, y=605)

img = PhotoImage(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=img, state='normal')

canvas.bind('<Button-1>',
            lambda event: click_left(event, figures, img, color_var, p_min, p_max, points_listbox))
canvas.bind('<Button-3>',
            lambda event: click_right(event, figures, img, color_var))

x_entry.insert(0, '100')
y_entry.insert(0, '100')

window.mainloop()
