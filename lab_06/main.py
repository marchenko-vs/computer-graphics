from constants import *
from tkinter import *
from draw import clear_canvas, click_left, click_wheel, click_right, draw_point, fill_figure

window = Tk()
window.title("Лабораторная работа #6")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
window.resizable(False, False)

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

figures = [[[]]]

Label(text="Цвет закраски", font=("Calibri", 18, "bold")).place(width=345, height=25, x=0, y=5)

color_var = IntVar()
color_var.set(5)

Radiobutton(text="Фиолетовый", variable=color_var, value=5,
            font=("Calibri", 16), anchor="w").place(width=150, height=20, x=20, y=40)

Radiobutton(text="Красный", variable=color_var, value=1,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=20, y=60)

Radiobutton(text="Синий", variable=color_var, value=2,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=20, y=80)

Radiobutton(text="Зеленый", variable=color_var, value=3,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=180, y=40)

Radiobutton(text="Желтый", variable=color_var, value=4,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=180, y=60)

Radiobutton(text="Черный", variable=color_var, value=0,
            font=("Calibri", 16), anchor="w").place(width=120, height=20, x=180, y=80)

Label(text="Режим закраски", font=("Calibri", 18, "bold")).place(width=345, height=30, x=0, y=105)

mode_var = BooleanVar()
mode_var.set(True)

Radiobutton(text="Без задержки", variable=mode_var, value=0,
            font=("Calibri", 16), anchor="w").place(width=150, height=20, x=20, y=140)

Radiobutton(text="С задержкой", variable=mode_var, value=1,
            font=("Calibri", 16), anchor="w").place(width=150, height=20, x=180, y=140)

Label(text="Построение точки", font=("Calibri", 18, "bold")).place(width=345, height=30, x=0, y=165)

Label(text="X", font=("Calibri", 16)).place(width=130, height=20, x=30, y=200)
Label(text="Y", font=("Calibri", 16)).place(width=130, height=20, x=195, y=200)

x_entry = Entry(font=("Calibri", 16), justify='center')
x_entry.place(width=125, height=30, x=30, y=230)

y_entry = Entry(font=("Calibri", 16), justify='center')
y_entry.place(width=125, height=30, x=195, y=230)

Button(text="Построить точку", font=("Calibri", 16),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda: draw_point(figures, img, x_entry, y_entry, points_listbox)). \
    place(width=290, height=35, x=30, y=265)

points_listbox = Listbox(font=("Calibri", 14))
points_listbox.place(width=290, height=125, x=30, y=305)

Button(text="Замкнуть фигуру", font=("Calibri", 16),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda event="<Button-3>": click_right(figures, img)). \
    place(width=290, height=35, x=30, y=435)

Label(text="Построение с помощью мыши",
      font=("Calibri", 18, "bold")).place(width=345, height=30, x=0, y=475)

Label(text="Левая кнопка - добавить точку",
      font=("Calibri", 16)).place(height=25, x=30, y=505)

Label(text="Правая кнопка - замкнуть фигуру",
      font=("Calibri", 16)).place(height=25, x=20, y=530)

Label(text="Время закраски:", font=("Calibri", 16)).place(width=150, height=30, x=20, y=560)

time_entry = Entry(font=("Calibri", 16))
time_entry.place(width=120, height=30, x=190, y=560)

Button(text="Выполнить\nзакраску", font=("Calibri", 16),
       highlightbackground="#d1d1e0", highlightthickness=30,
       command=lambda: fill_figure(figures, img, canvas, color_var, mode_var, time_entry, seed_pixel)). \
    place(width=145, height=50, x=25, y=595)

Button(text="Очистить\nэкран", font=("Calibri", 16),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda: clear_canvas(img, figures, time_entry, points_listbox, seed_pixel)). \
    place(width=145, height=50, x=180, y=595)

img = PhotoImage(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=img, state='normal')

seed_pixel = [-1, -1]

canvas.bind('<Button-1>',
            lambda event: click_left(event, figures, img, points_listbox))
canvas.bind('<Button-2>',
            lambda event: click_wheel(event, seed_pixel, img, color_var, points_listbox))
canvas.bind('<Button-3>',
            lambda event: click_right(figures, img))

x_entry.insert(0, '100')
y_entry.insert(0, '100')

window.mainloop()
