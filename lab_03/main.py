from tkinter import *
from tkinter import messagebox
from math import fabs, ceil, radians, cos, sin, floor
import matplotlib.pyplot as plt
import time

from CDA import cda_test, draw_line_cda
from BresenhamFloat import float_test, draw_line_brez_float
from BresenhamInt import int_test, draw_line_brez_int
from BresenhamSmooth import smoth_test
from Wu import vu_test

from calculations import sign, get_rgb_intensity


canvW, canvH = 1500, 990
line_r = 150


def draw_line_brez_smoth(canvas, ps, pf, fill):
    I = 100
    fill = get_rgb_intensity(canvas, fill, bg_color, I)
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        steep = 1 #
    else:
        steep = 0 #
    tg = dy / dx * I # тангенс угла наклона (умножаем на инт., чтобы не приходилось умножать внутри цикла
    e = I / 2 # интенсивность для высвечивания начального пикселя
    w = I - tg # пороговое значение
    x = ps[0]
    y = ps[1]
    stairs = []
    st = 1
    while x != pf[0] or y != pf[1]:
        canvas.create_line(x, y, x + 1, y + 1, fill=fill[round(e) - 1])
        if e < w:
            if steep == 0: # dy < dx
                x += sx # -1 if dx < 0, 0 if dx = 0, 1 if dx > 0
            else: # dy >= dx
                y += sy # -1 if dy < 0, 0 if dy = 0, 1 if dy > 0
            st += 1 # stepping
            e += tg
        elif e >= w:
            x += sx
            y += sy
            e -= w
            stairs.append(st)
            st = 0
    if st:
        stairs.append(st)
    return stairs


def draw_line_vu(canvas, ps, pf, fill):
    x1 = ps[0]
    x2 = pf[0]
    y1 = ps[1]
    y2 = pf[1]
    I = 100
    stairs = []
    fills = get_rgb_intensity(canvas, fill, bg_color, I)
    if x1 == x2 and y1 == y2:
        canvas.create_line(x1, y1, x1 + 1, y1 + 1, fill = fills[100])

    steep = abs(y2 - y1) > abs(x2 - x1)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        tg = 1
    else:
        tg = dy / dx

    # first endpoint
    xend = round(x1)
    yend = y1 + tg * (xend - x1)
    xpx1 = xend
    y = yend + tg

    # second endpoint
    xend = int(x2 + 0.5)
    xpx2 = xend
    st = 0

    # main loop
    if steep:
        for x in range(xpx1, xpx2):
            canvas.create_line(int(y), x + 1, int(y) + 1, x + 2,
                               fill = fills[int((I - 1) * (abs(1 - y + int(y))))])
            canvas.create_line(int(y) + 1, x + 1, int(y) + 2, x + 2,
                               fill = fills[int((I - 1) * (abs(y - int(y))))])

            if (abs(int(x) - int(x + 1)) >= 1 and tg > 1) or \
                    (not 1 > abs(int(y) - int(y + tg)) >= tg):
                stairs.append(st)
                st = 0
            else:
                st += 1
            y += tg
    else:
        for x in range(xpx1, xpx2):
            #print((I - 1)*round(abs(1 - y + floor(y))))
            canvas.create_line(x + 1, int(y), x + 2, int(y) + 1,
                               fill = fills[round((I - 1) * (abs(1 - y + floor(y))))])
            #print((I - 1)*round(abs(y - floor(y))))
            canvas.create_line(x + 1, int(y) + 1, x + 2, int(y) + 2,
                               fill = fills[round((I - 1) * (abs(y - floor(y))))])

            if (abs(int(x) - int(x + 1)) >= 1 and tg > 1) or \
                    (not 1 > abs(int(y) - int(y + tg)) >= tg):
                stairs.append(st)
                st = 0
            else:
                st += 1
            y += tg
    return stairs


# Получение параметров для отрисовки
def draw(test_mode):
    choise = method_list.curselection()
    if len(choise) == 1:
        xs, ys = fxs.get(), fys.get()
        xf, yf = fxf.get(), fyf.get()
        if not xs and not ys:
            messagebox.shorerror('Ошибка!',
                                   'Не заданы координаты начала отрезка.')
        elif not xs or not ys:
            messagebox.shorerror('Ошибка!',
                                   'Не задана одна из координат начала отрезка.')
        elif not xf and not yf:
            messagebox.shorerror('Ошибка!',
                                   'Не заданы координаты конца отрезка.')
        elif not xf or not yf:
            messagebox.shorerror('Ошибка!',
                                   'Не задана одна из координат конца отрезка.')
        else:
            try:
                xs, ys = round(float(xs)), round(float(ys))
                xf, yf = round(float(xf)), round(float(yf))
                if xs != xf or ys != yf:
                    if not test_mode:
                        if choise[0] == 5:
                            canvas.create_line([xs, ys], [xf, yf], fill=line_color)
                        else:
                            funcs[choise[0]](canvas, [xs, ys], [xf, yf], fill=line_color)
                    else:
                        angle = fangle.get()
                        if angle:
                            try:
                                angle = float(angle)
                            except:
                                messagebox.showerror('Ошибка!',
                                                      'Введено нечисловое значение угла поворота.')
                            if angle:
                                angle = round(angle)
                                test(1, choise[0], funcs[choise[0]], angle, [xs, ys], [xf, yf])
                            else:
                                messagebox.showerror('Ошибка!',
                                                           'Задано нулевое значение для угла поворота.')

                        else:
                            messagebox.showerror('Ошибка!',
                                                   'Не задано значение угла поворота.')
                else:
                    messagebox.showerror('Ошибка!',
                                           'Начало и конец отрезка совпадают.')
            except ValueError:
                messagebox.showerror('Ошибка!',
                                     'Введено нечисловое значение одной из координат начала или конца отрезка.')
    elif not len(choise):
        messagebox.showerror('Ошибка!',
                               'Не выбран метод построения отрезка.')
    else:
        messagebox.showerror('Ошибка!',
                               'Выбрано более одного метода простроения отрезка.')


# Получение параметров для анализа
def analyze(mode):
    try:
        length = len_line.get()
        if length:
            length = round(float(length))
        else:
            length = 100
        if not mode:
            time_bar(length)
        else:
            ind = method_list.curselection()
            if ind:
                if ind[-1] != 5:
                    smoth_analyze(ind, length)
                else:
                    messagebox.showwarning('Предупреждение!',
                                           'Библиотечный метод не может '
                                           'быть проанализирован на ступенчатость.')
            else:
                messagebox.showwarning('Предупреждение!',
                                       'Не выбран метод построения отрезка.')
    except ValueError:
        messagebox.showerror('Ошибка!',
                             'Введено нечисловое значение длины отрезка.')


# замер времени
def test(flag, ind, method, angle, pb, pe):
    global line_color

    total = 0
    steps = int(360 // angle)
    for i in range(steps):
        cur1 = time.time()
        if flag == 0:
            #method(pb, pe)
            method(canvas, pb, pe, fill=bg_color)#line_color)
        else:
            method(canvas, pb, pe, fill=line_color)
        cur2 = time.time()
        turn_point(radians(angle), pe, pb)
        total += cur2 - cur1

    return total / steps


# гистограмма времени
def time_bar(length):
    close_plt()
    plt.figure(2, figsize=(9, 7))
    times = []
    angle = 1
    pb = [center[0], center[1]]
    pe = [center[0] + 100, center[1]]
    for i in range(5):
#        times.append(test(0, i, test_funcs[i], angle, pb, pe))
        times.append(test(0, i, funcs[i], angle, pb, pe))
    clean()
    Y = range(len(times))
    L = ('ЦДА', 'Брезенхем\n(действительные\nданные)',
         'Брезенхем\n(целочисленные\nданные)', 'Брезенхем\n(устранение\nступенчатости)', 'Ву')
    plt.bar(Y, times, align='center')
    plt.xticks(Y, L)
    plt.ylabel("Время в секундах (длина отрезка - " + str(length) + " пикселей)")
    plt.show()


# Поворот точки для сравнения ступенчатости
def turn_point(angle, p, center):
    x = p[0]
    p[0] = round(center[0] + (x - center[0]) * cos(angle) + (p[1] - center[1]) * sin(angle))
    p[1] = round(center[1] - (x - center[0]) * sin(angle) + (p[1] - center[1]) * cos(angle))


# Анализ ступечатости
def smoth_analyze(methods, length):
    close_plt()
    names = ('ЦДА', 'Брезенхем\n(действительные\nданные)',
             'Брезенхем\n(целочисленные\nданные)', 'Брезенхем\n(устранение\nступенчатости)', 'Ву')
    plt.figure(1)
    plt.title("Анализ ступенчатости")
    plt.xlabel("Угол, градусы")
    plt.ylabel("Количество ступеней (длина отрезка - " + str(length) + " пикселей)")
    plt.grid(True)
    plt.legend(loc='best')

    for i in methods:
        max_len = []
        nums = []
        angles = []
        angle = 0
        step = 2
        pb = [center[0], center[1]]
        pe = [center[0] + length, center[1]]

        for j in range(90 // step):
            stairs = funcs[i](canvas, pb, pe, line_color)
            turn_point(radians(step), pe, pb)
            if stairs:
                max_len.append(max(stairs))
            else:
                max_len.append(0)
            nums.append(len(stairs))
            angles.append(angle)
            angle += step
        clean()
        plt.figure(1)
        plt.plot(angles, nums, label=names[i])
        plt.legend()
    plt.show()


def draw_axes():
    return
    color = 'gray'
    canvas.create_line(0, 2, canvW, 2, fill="darkred", arrow=LAST)
    canvas.create_line(2, 0, 2, canvH, fill="darkred", arrow=LAST)
    for i in range(50, canvW, 50):
        canvas.create_text(i, 10, text=str(abs(i)), fill=color)
        canvas.create_line(i, 0, i, 5, fill=color)

    for i in range(50, canvH, 50):
        canvas.create_text(15, i, text=str(abs(i)), fill=color)
        canvas.create_line(0, i, 5, i, fill=color)


def clean():
    canvas.delete("all")
    draw_axes()


def show_info():
    messagebox.showinfo('Справочная информация.',
                        'С помощью данной программы можно построить отрезки шестью методами.\n'
                        '1. Методом цифрового дифференциального анализатора.\n'
                        '2. Методом Брезенхема с действительными данными.\n'
                        '3. Методом Брезенхема с целочисленными данными.\n'
                        '4. Методом Брезенхема со сглаживанием.\n'
                        '5. Методом Ву.\n'
                        '6. Стандартым методом из библиотеки.\n\n'
                        'Для построения отрезка необходимо задать координаты его начала\n'
                        'и конца и выбрать метод построения из списка предложенных.\n\n'
                        'Для визуального анализа (построения пучка лучей)\n'
                        'необходимо задать координаты начала и конца,\n'
                        'выбрать метод построения отрезка для анализа,\n'
                        'а также угол поворота отрезков.\n\n'
                        'Для анализа ступенчатости можно выбрать сразу несколько методов.\n'
                        'Чтобы это сделать, зажмите клавишу Shift при выборе.\n'
                        'Введите длину отрезка, если хотите сделать анализ программы\n'
                        'при построении отрезков определенной длины.')


def fill_list(lst):
    lst.insert(END, "Цифровой дифференциальный анализатор")
    lst.insert(END, "Брезенхем с действительными данными")
    lst.insert(END, "Брезенхем с целочисленными данными")
    lst.insert(END, "Брезенхем с устранением ступенчатости")
    lst.insert(END, "Алгоритм Ву")
    lst.insert(END, "Библиотечная реализация (Python Tkinter)")


def set_bgcolor(color):
    global bg_color
    bg_color = color
    canvas.configure(bg=bg_color)


def set_linecolor(color):
    global line_color
    line_color = color
    lb_lcolor.configure(bg=line_color)


def close_plt():
    plt.figure(1)
    plt.close()
    plt.figure(2)
    plt.close()


def close_all():
    if messagebox.askyesno("Выход", "Вы действительно хотите завершить программу?"):
        close_plt()
        root.destroy()


root = Tk()
root.geometry('1900x1000+0+0')
root.resizable(0, 0)
root.title('Лабораторная работа #3')

color_menu = "#7586c5"

x_menu = 10
w_menu = 375

# Фрейм для выбора цвета
color_frame = Frame(root, height=400, width=w_menu)
color_frame.place(x=x_menu, y=740)

canv = Canvas(root, width=canvW, height=canvH, bg='white')
canvas = canv
canvas_test = canv
canv.pack(side='right')
center = (375, 200)

# Список алгоритмов
method_list = Listbox(root, selectmode=EXTENDED, font='Calibri 14')
method_list.place(x=x_menu, y=10, width=w_menu, height=150)
fill_list(method_list)

funcs = (draw_line_cda, draw_line_brez_float, draw_line_brez_int,
         draw_line_brez_smoth, draw_line_vu, canvas.create_line)
test_funcs = (cda_test, float_test, int_test, smoth_test, vu_test)

# Координаты начала и конца отрезка
lb1 = Label(text='Начало отрезка', font='Calibri 14')
lb1.place(x=130, y=180)

lbx1 = Label(text='X', font='Calibri 14')
lbx1.place(x=40, y=220)

fxs = Entry(font='Calibri 14', justify='center')
fxs.place(x=70, y=220, width=100)

lby1 = Label(text='Y', font='Calibri 14')
lby1.place(x=190, y=220)

fys = Entry(font='Calibri 14', justify='center')
fys.place(x=220, y=220, width=100)

lb2 = Label(text='Конец отрезка', font='Calibri 14')
lb2.place(x=130, y=260)

lbx2 = Label(text='X', font='Calibri 14')
lbx2.place(x=40, y=300)

fxf = Entry(font='Calibri 14', justify='center')
fxf.place(x=70, y=300, width=100)

lby2 = Label(text='Y', font='Calibri 14')
lby2.place(x=190, y=300)

fyf = Entry(font='Calibri 14', justify='center')
fyf.place(x=220, y=300, width=100)

btn_draw = Button(text="Построить отрезок", font='Calibri 14',
                  command=lambda: draw(0), width=140, height=25)
btn_draw.place(x=110, y=350, width=180, height=40)

fxs.insert(0, str(canvW / 2))
fys.insert(0, str(canvH / 2))

fxf.insert(0, str(canvW / 2 + line_r))
fyf.insert(0, str(canvH / 2 + line_r))

# Поворот
lb_angle = Label(text="Угол поворота (в градусах)",
                 font='Calibri 14')
lb_angle.place(x=90, y=420)

fangle = Entry(font='Calibri 14', justify='center')
fangle.place(x=105, y=460, width=200)
fangle.insert(0, "15.0")

btn_viz = Button(text="Построить пучок лучей", 
                 font='Calibri 14', command=lambda: draw(1))
btn_viz.place(x=105, y=500, width=200)

# Анализ алгоритмов
lb_len = Label(text="Длина отрезка\n(по умолчанию - 100)",
               font='Calibri 14')
lb_len.place(x=110, y=560)

len_line = Entry(font='Calibri 14', justify='center')
len_line.place(x=110, y=620, width=180)

btn_time = Button(text="Сравнение\nвремени",
                  font='Calibri 14', command=lambda: analyze(0))
btn_time.place(x=40, y=660, width=140, height=50)

btn_smoth = Button(text="Сравнение\nступенчатости", 
                   font='Calibri 14', command=lambda: analyze(1))
btn_smoth.place(x=210, y=660, width=140, height=50)

# Дополнительные кнопки
btn_clean = Button(text="Очистить экран", font='Calibri 14',
                   command=clean)
btn_clean.place(x=50, y=950, width=140)

btn_help = Button(text="Информация", font='Calibri 14',
                  command=show_info)
btn_help.place(x=210, y=950, width=140)

# Цвета
line_color = 'black'
bg_color = 'white'

size = 30

white_line = Button(color_frame, bg="white", activebackground="white",
                    command=lambda: set_linecolor('white'))
white_line.place(x=60, y=50, height=size, width=size)

black_line = Button(color_frame, bg="yellow", activebackground="black",
                    command=lambda: set_linecolor("yellow"))

black_line.place(x=90, y=50, height=size, width=size)

red_line = Button(color_frame, bg="orange", activebackground="orange",
                  command=lambda: set_linecolor("orange"))
red_line.place(x=120, y=50, height=size, width=size)

orange_line = Button(color_frame, bg="red", activebackground="red",
                     command=lambda: set_linecolor("red"))
orange_line.place(x=150, y=50, height=size, width=size)

yellow_line = Button(color_frame, bg="purple", activebackground="purple",
                     command=lambda: set_linecolor("purple"))
yellow_line.place(x=180, y=50, height=size, width=size)

green_line = Button(color_frame, bg="darkblue", activebackground="darkblue",
                    command=lambda: set_linecolor("darkblue"))
green_line.place(x=210, y=50, height=size, width=size)

doger_line = Button(color_frame, bg="darkgreen", activebackground="darkgreen",
                    command=lambda: set_linecolor("darkgreen"))
doger_line.place(x=240, y=50, height=size, width=size)

blue_line = Button(color_frame, bg="black", activebackground="black",
                   command=lambda: set_linecolor("black"))
blue_line.place(x=270, y=50, height=size, width=size)

white_bg = Button(color_frame, bg="white", activebackground="white",
                  command=lambda: set_bgcolor("white"))
white_bg.place(x=60, y=140, height=size, width=size)
black_bg = Button(color_frame, bg="yellow", activebackground="yellow",
                  command=lambda: set_bgcolor("yellow"))
black_bg.place(x=90, y=140, height=size, width=size)
red_bg = Button(color_frame, bg="orange", activebackground="orange",
                command=lambda: set_bgcolor("orange"))
red_bg.place(x=120, y=140, height=size, width=size)
orange_bg = Button(color_frame, bg="red", activebackground="red",
                   command=lambda: set_bgcolor("red"))
orange_bg.place(x=150, y=140, height=size, width=size)
yellow_bg = Button(color_frame, bg="purple", activebackground="purple",
                   command=lambda: set_bgcolor("purple"))
yellow_bg.place(x=180, y=140, height=size, width=size)
green_bg = Button(color_frame, bg="darkblue", activebackground="darkblue",
                  command=lambda: set_bgcolor("darkblue"))
green_bg.place(x=210, y=140, height=size, width=size)
dodger_bg = Button(color_frame, bg="darkgreen", activebackground="darkgreen",
                   command=lambda: set_bgcolor("darkgreen"))
dodger_bg.place(x=240, y=140, height=size, width=size)

blue_bg = Button(color_frame, bg="black", activebackground="black",
                 command=lambda: set_bgcolor("black"))
blue_bg.place(x=270, y=140, height=size, width=size)

lb_line = Label(color_frame, text='Цвет отрезка (текущий:       )',
                font='Calibri 14')
lb_line.place(x=70, y=10)

lb_lcolor = Label(color_frame, bg=line_color)
lb_lcolor.place(x=265, y=18, width=15, height=15)

lb_bg = Label(color_frame, text='Цвет фона', font='Calibri 14')
lb_bg.place(x=140, y=100)

draw_axes()
root.mainloop()
