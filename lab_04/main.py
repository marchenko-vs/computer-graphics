from tkinter import *
from draw import draw_figure, draw_spectrum, clear_canvas
from comparisons import time_comparison

from constants import *

spectrum_var_arr = list()
spectrum_entry_arr = list()
spectrum_widget_arr = list()


def change_figure(rb_entry, figure):
    if figure.get():
        rb_entry.configure(state=NORMAL)
        draw_fields_for_ellipse()
    else:
        rb_entry.configure(state=DISABLED)
        draw_fields_for_circle()


def change_spectrum_entry(step_x_entry, step_y_entry, step_BooleanVar):
    if step_BooleanVar.get():
        step_y_entry.configure(state=NORMAL)
        step_x_entry.configure(state=DISABLED)
    else:
        step_x_entry.configure(state=NORMAL)
        step_y_entry.configure(state=DISABLED)


def activate_fields(spectrum_entry, is_activate):
    if is_activate:
        spectrum_entry.configure(state=NORMAL)
    else:
        spectrum_entry.configure(state=DISABLED)


def choice_fields(spectrum_var_arr, spectrum_entry_arr, index_method):
    if spectrum_var_arr[index_method].get():
        spectrum_var_arr[index_method].set(0)
        return

    size = len(spectrum_var_arr)

    for i in range(size):
        if i != index_method and spectrum_var_arr[i].get() == False:
            spectrum_var_arr[i].set(1)
            activate_fields(spectrum_entry_arr[i], True)

    activate_fields(spectrum_entry_arr[index_method], False)


def place_forget(spectrum_entry_arr, spectrum_widget_arr):
    for i in spectrum_entry_arr:
        i.place_forget()

    for i in spectrum_widget_arr:
        i.place_forget()


def draw_fields_for_circle():
    global spectrum_var_arr, spectrum_entry_arr, spectrum_widget_arr

    place_forget(spectrum_entry_arr, spectrum_widget_arr)

    beg_radius_intvar = IntVar()
    end_radius_intvar = IntVar()
    step_intvar = IntVar()
    count_figure_intvar = IntVar()

    beg_radius_intvar.set(1)
    step_intvar.set(1)
    count_figure_intvar.set(1)

    beg_radius_Checkbutton = Checkbutton(
        text="Начальный радиус:",
        variable=beg_radius_intvar,
        font=("Calibri", 16), anchor="w",
        command=lambda: choice_fields(spectrum_var_arr, spectrum_entry_arr, 0))
    beg_radius_Checkbutton.place(width=200, height=30, x=10, y=435)

    end_radius_Checkbutton = Checkbutton(
        text="Конечный радиус:",
        variable=end_radius_intvar,
        font=("Calibri", 16), anchor="w",
        command=lambda: choice_fields(spectrum_var_arr, spectrum_entry_arr, 1))
    end_radius_Checkbutton.place(width=200, height=30, x=10, y=465)

    step_Checkbutton = Checkbutton(
        text="Шаг построения:",
        variable=step_intvar,
        font=("Calibri", 16), anchor="w",
        command=lambda: choice_fields(spectrum_var_arr, spectrum_entry_arr, 2))
    step_Checkbutton.place(width=200, height=30, x=10, y=495)

    count_figure_Checkbutton = Checkbutton(
        text="Количество фигур:",
        variable=count_figure_intvar,
        font=("Calibri", 16), anchor="w",
        command=lambda: choice_fields(spectrum_var_arr, spectrum_entry_arr, 3))
    count_figure_Checkbutton.place(width=200, height=30, x=10, y=525)

    beg_radius_entry = Entry(font=("Calibri", 16), justify='center')
    beg_radius_entry.place(width=60, height=30, x=240, y=435)

    end_radius_entry = Entry(font=("Calibri", 16), justify='center')
    end_radius_entry.place(width=60, height=30, x=240, y=465)

    step_entry = Entry(font=("Calibri", 16), justify='center')
    step_entry.place(width=60, height=30, x=240, y=495)

    count_figure_entry = Entry(font=("Calibri", 16), justify='center')
    count_figure_entry.place(width=60, height=30, x=240, y=525)

    step_entry.insert(0, '10')
    count_figure_entry.insert(0, '15')

    beg_radius_entry.insert(0, '200')
    end_radius_entry.insert(0, '340')
    end_radius_entry.configure(state=DISABLED)

    spectrum_var_arr = [beg_radius_intvar, end_radius_intvar,
                        step_intvar, count_figure_intvar]
    spectrum_entry_arr = [beg_radius_entry, end_radius_entry,
                          step_entry, count_figure_entry]
    spectrum_widget_arr = [beg_radius_Checkbutton, end_radius_Checkbutton,
                           step_Checkbutton, count_figure_Checkbutton]


def draw_fields_for_ellipse():
    global spectrum_var_arr, spectrum_entry_arr, spectrum_widget_arr

    place_forget(spectrum_entry_arr, spectrum_widget_arr)

    step_BooleanVar = BooleanVar()
    step_BooleanVar.set(False)

    radius_x_Label = Label(
        text="Начальное значение Rx:",
        font=("Calibri", 16), anchor="w")
    radius_x_Label.place(width=220, height=30, x=10, y=435)

    radius_y_Label = Label(
        text="Начальное значение Ry:",
        font=("Calibri", 16), anchor="w")
    radius_y_Label.place(width=220, height=30, x=10, y=465)

    step_x_Radiobutton = Radiobutton(
        text="Шаг построения ΔRx:",
        variable=step_BooleanVar, value=0,
        font=("Calibri", 16), anchor="w",
        command=lambda: change_spectrum_entry(step_x_entry, step_y_entry, step_BooleanVar))
    step_x_Radiobutton.place(width=220, height=30, x=10, y=495)

    step_y_Radiobutton = Radiobutton(
        text="Шаг построения ΔRy:",
        variable=step_BooleanVar, value=1,
        font=("Calibri", 16), anchor="w",
        command=lambda: change_spectrum_entry(step_x_entry, step_y_entry, step_BooleanVar))
    step_y_Radiobutton.place(width=220, height=30, x=10, y=525)

    count_figure_Label = Label(
        text="Количество фигур:",
        font=("Calibri", 16), anchor="w")
    count_figure_Label.place(width=200, height=30, x=10, y=555)

    radius_x_entry = Entry(font=("Calibri", 16), justify='center')
    radius_x_entry.place(width=60, height=30, x=240, y=435)

    radius_y_entry = Entry(font=("Calibri", 16), justify='center')
    radius_y_entry.place(width=60, height=30, x=240, y=465)

    step_x_entry = Entry(font=("Calibri", 16), justify='center')
    step_x_entry.place(width=60, height=30, x=240, y=495)

    step_y_entry = Entry(font=("Calibri", 16), justify='center')
    step_y_entry.place(width=60, height=30, x=240, y=525)

    count_figure_entry = Entry(font=("Calibri", 16), justify='center')
    count_figure_entry.place(width=60, height=30, x=240, y=555)

    radius_x_entry.insert(0, '200')
    radius_y_entry.insert(0, '100')

    count_figure_entry.insert(0, '20')
    step_x_entry.insert(0, '10')
    step_y_entry.insert(0, '10')
    step_y_entry.configure(state=DISABLED)

    spectrum_var_arr = [step_BooleanVar]
    spectrum_entry_arr = [radius_x_entry, radius_y_entry, step_x_entry, step_y_entry,
                          count_figure_entry]
    spectrum_widget_arr = [radius_x_Label, radius_y_Label, step_x_Radiobutton, step_y_Radiobutton,
                           count_figure_Label]


window = Tk()
window.title("Лабораторная работа #4")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
window.resizable(False, False)

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack(side='right')

Label(text="Цвет фигур", font=("Calibri", 18, 'bold')).place(width=295, height=25, x=0, y=5)

color_fg = IntVar()
color_fg.set(0)

Radiobutton(text="Чёрный", variable=color_fg, value=0,
            font=("Calibri", 16), anchor="w").place(width=110, height=20, x=20, y=35)

Radiobutton(text="Фоновый", variable=color_fg, value=1,
            font=("Calibri", 16), anchor="w").place(width=110, height=20, x=20, y=55)

Radiobutton(text="Красный", variable=color_fg, value=2,
            font=("Calibri", 16), anchor="w").place(width=110, height=20, x=170, y=35)

Radiobutton(text="Синий", variable=color_fg, value=3,
            font=("Calibri", 16), anchor="w").place(width=110, height=20, x=170, y=55)

Label(text="Алгоритм построения", font=("Calibri", 18, "bold")).place(width=295, height=25, x=0, y=80)

algorithm = IntVar()
algorithm.set(0)

Radiobutton(text="Каноническое уравнение", variable=algorithm, value=0,
            font=("Calibri", 16), anchor="w").place(width=260, height=20, x=10, y=110)

Radiobutton(text="Параметрическое уравнение", variable=algorithm, value=1,
            font=("Calibri", 16), anchor="w").place(width=290, height=20, x=10, y=130)

Radiobutton(text="Алгоритм Брезенхема", variable=algorithm, value=2,
            font=("Calibri", 16), anchor="w").place(width=260, height=20, x=10, y=150)

Radiobutton(text="Алгоритм средней точки", variable=algorithm, value=3,
            font=("Calibri", 16), anchor="w").place(width=260, height=20, x=10, y=170)

Radiobutton(text="Библиотечная функция", variable=algorithm, value=4,
            font=("Calibri", 16), anchor="w").place(width=260, height=20, x=10, y=190)

Label(text="Выбор фигуры", font=("Calibri", 18, "bold")).place(width=305, height=25, x=0, y=215)

figure = BooleanVar()
figure.set(False)

Radiobutton(text="Окружность", variable=figure, value=0,
            font=("Calibri", 16), anchor="w",
            command=lambda: change_figure(rb_entry, figure)).place(width=150, height=20, x=20, y=245)

Radiobutton(text="Эллипс", variable=figure, value=1,
            font=("Calibri", 16), anchor="w",
            command=lambda: change_figure(rb_entry, figure)).place(width=110, height=20, x=180, y=245)

Label(text="Построение фигуры", font=("Calibri", 18, "bold")).place(width=305, height=25, x=0, y=270)

Label(text="Xc", font=("Calibri", 16)).place(height=20, x=30, y=300)
Label(text="Yc", font=("Calibri", 16)).place(height=20, x=105, y=300)
Label(text="Rx", font=("Calibri", 16)).place(height=20, x=180, y=300)
Label(text="Ry", font=("Calibri", 16)).place(height=20, x=255, y=300)

xc_entry = Entry(font=("Calibri", 16), justify='center')
xc_entry.place(width=65, height=30, x=10, y=325)

yc_entry = Entry(font=("Calibri", 16), justify='center')
yc_entry.place(width=65, height=30, x=85, y=325)

ra_entry = Entry(font=("Calibri", 16), justify='center')
ra_entry.place(width=65, height=30, x=160, y=325)

rb_entry = Entry(font=("Calibri", 16), justify='center')
rb_entry.place(width=65, height=30, x=235, y=325)

Button(text="Построить фигуру", font=("Calibri", 17),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda: draw_figure(canvas, color_fg, algorithm, figure,
                                   xc_entry, yc_entry, ra_entry, rb_entry)). \
    place(width=290, height=33, x=10, y=365)

Label(text="Построение спектра", font=("Calibri", 18, "bold")).place(width=305, height=25, x=0, y=405)

Button(text="Построить cпектр", font=("Calibri", 17),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda: draw_spectrum(canvas, color_fg, algorithm, figure,
                                     xc_entry, yc_entry, spectrum_var_arr, spectrum_entry_arr)). \
    place(width=290, height=33, x=10, y=590)

Button(text="Сравнение времени", font=("Calibri", 17),
       highlightbackground="#d1d1e0", highlightthickness=30,
       command=lambda: time_comparison(canvas, color_fg, algorithm, figure)).place(width=290, height=33, x=10, y=625)

Button(text="Очистить экран", font=("Calibri", 17),
       highlightbackground="#b3b3cc", highlightthickness=30,
       command=lambda: clear_canvas(canvas)).place(width=290, height=33, x=10, y=660)

xc_entry.insert(0, CANVAS_WIDTH // 2)
yc_entry.insert(0, CANVAS_HEIGHT // 2)

ra_entry.insert(0, '150')
rb_entry.insert(0, '100')
rb_entry.configure(state=DISABLED)

change_figure(rb_entry, figure)

window.mainloop()
