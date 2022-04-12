import matplotlib.pyplot as plt
import time
from tkinter import *
from tkinter import messagebox

from bresenham import *
from constants import *
from dda import cda_test, draw_line_cda
from graphics_math import sign, get_rgb_intensity
from math import fabs, ceil, radians, cos, sin, floor
from wu import vu_test


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
    choice = method_list.curselection()

    if len(choice) == 1:
        xs, ys = fxs.get(), fys.get()
        xf, yf = fxf.get(), fyf.get()

        if not xs and not ys:
            messagebox.showwarning('Ошибка ввода',
                                   'Не заданы координаты начала отрезка!')
        elif not xs or not ys:
            messagebox.showwarning('Ошибка ввода',
                                   'Не задана одна из координат начала отрезка!')
        elif not xf and not yf:
            messagebox.showwarning('Ошибка ввода',
                                   'Не заданы координаты конца отрезка!')
        elif not xf or not yf:
            messagebox.showwarning('Ошибка ввода',
                                   'Не задана одна из координат конца отрезка!')
        else:
            #try:
                xs, ys = round(float(xs)), round(float(ys))
                xf, yf = round(float(xf)), round(float(yf))

                if xs != xf or ys != yf:
                    if not test_mode:
                        if choice[0] == 5:
                            canvas.create_line([xs, ys], [xf, yf], fill=line_color)
                        else:
                            funcs[choice[0]](canvas, [xs, ys], [xf, yf], fill=line_color)
                    else:
                        angle = fangle.get()
                        if angle:
                            try:
                                angle = int(angle)
                            except:
                                messagebox.showerror('Ошибка!',
                                                     'Введено нечисловое значение для шага анализа!')
                            if angle:
                                test(1, choice[0], funcs[choice[0]], angle, [xs, ys], [xf, yf])
                            else:
                                messagebox.showwarning('Ошибка!',
                                                       'Задано нулевое значение для угла поворота!')

                        else:
                            messagebox.showwarning('Ошибка ввода',
                                                   'Не задано значение для шага анализа!')
                else:
                    messagebox.showwarning('Ошибка ввода',
                                           'Начало и конец отрезка совпадают!')
            #except:
                #messagebox.showwarning('Ошибка ввода',
                #                       'Нечисловое значение для параметров отрезка!')
    elif not len(choice):
        messagebox.showerror('Ошибка!',
                             'Не выбран алгоритм построения отрезка.')
    else:
        messagebox.showerror('Ошибка!',
                             'Выбрано более одного алгоритма простроения отрезка.')


# Получение параметров для анализа
def analyze(mode):
    try:
        length = len_line.get()

        if length:
            length = int(length)
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
                    messagebox.showwarning('Предупреждение',
                                           'Стандартный метод не может '
                                           'быть проанализирован на ступенчатость!')
            else:
                messagebox.showwarning('Предупреждение',
                                       'Не выбрано ни одного'
                                       'метода построения отрезка!')
    except ValueError:
        messagebox.showerror('Ошибка!',
                             'Длина отрезка должна быть целым числом.')


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
    L = ('Digital\ndifferential\nanalyzer', 'Bresenham\n(real coeffs)',
         'Bresenham\n(int coeffs)', 'Bresenham\n(smooth)', 'Wu')
    plt.bar(Y, times, align='center')
    plt.xticks(Y, L)
    plt.ylabel("Work time in sec. (line len. " + str(length) + ")")
    plt.show()

# Поворот точки для сравнения ступенчатости
def turn_point(angle, p, center):
    x = p[0]
    p[0] = round(center[0] + (x - center[0]) * cos(angle) + (p[1] - center[1]) * sin(angle))
    p[1] = round(center[1] - (x - center[0]) * sin(angle) + (p[1] - center[1]) * cos(angle))

# Анализ ступечатости
def smoth_analyze(methods, length):
    close_plt()
    names = ('Digital\ndifferential\nanalyzer', 'Bresenham\n(real coeffs)',
             'Bresenham\n(int coeffs)', 'Bresenham\n(smooth)', 'Wu')
    plt.figure(1)
    plt.title("Stepping analysis")
    plt.xlabel("Angle")
    plt.ylabel("Number of steps(line length " + str(length) + ")")
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

# Оси координат
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

# очистка холста
def clean():
    canvas.delete("all")
    draw_axes()

# Справка
def show_info():
    messagebox.showinfo('Информация.',
                        'С помощью данной программы можно построить отрезки шестью алгоритмами:\n'
                        '1. Алгоритмом цифрового дифференциального анализатора.\n'
                        '2. Алгоритмом Брезенхема с действитльными коэффициентами.\n'
                        '3. Алгоритмом Брезенхема с целыми коэффициентами.\n'
                        '4. Алгоритмом Брезенхема со сглаживанием.\n'
                        '5. Алгоритмом Ву.\n'
                        '6. Стандартым алгоритмом из библиотеки.\n\n'
                        'Для построения отрезка необходимо задать его начало\n'
                        'и конец и выбрать метод построения из списка предложенных.\n\n'
                        'Для визуального анализа (построения пучка отрезков)\n'
                        'необходимо задать начало и конец,\n'
                        'выбрать метод для анализа,\n'
                        'а также угол поворота отрезка.\n\n'
                        'Для анализа ступенчатости можно выбрать сразу несколько методов.\n'
                        'Чтобы это сделать, зажмите SHIFT при выборе.\n'
                        'Анализ ступенчатости и времени исполнения приводится\n'
                        'в виде графиков pyplot.\n'
                        'Введите длину отрезка, если хотите сделать анализ программы\n'
                        'при построении отрезков определенной длины.')

# Список методов прорисовки отрезка
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


main_window = Tk()
main_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0')
main_window.resizable(width=False, height=False)
main_window.title('Лабораторная работа #3')

# Коэффициенты для отезка
coords_frame = Frame(main_window, height=200, width=MENU_WIDTH)
coords_frame.place(x=10, y=110)

# угол
angle_frame = Frame(main_window, height=200, width=MENU_WIDTH)
angle_frame.place(x=10, y=210)

# выбор цвета
color_frame = Frame(main_window, height=150, width=MENU_WIDTH)
color_frame.place(x=10, y=300)

# сравнение
comparison_frame = Frame(main_window, height=200, width=MENU_WIDTH)
comparison_frame.place(x=10, y=750)

# очистить, справка
menu_frame = Frame(main_window, height=50, width=MENU_WIDTH)
menu_frame.place(x=10, y=940)

# Холст
canv = Canvas(main_window, width=CANVAS_WIDTH,
              height=CANVAS_HEIGHT, bg='white')
canvas = canv
canvas_test = canv # Удалить
# canv.place(x=0, y=000)
canv.pack(side='right')
center = (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)

# Список алгоритмов
method_list = Listbox(main_window, selectmode=EXTENDED, font='Calibri 12')
method_list.place(x=10, y=10, width=MENU_WIDTH, height=130)
fill_list(method_list)
funcs = (draw_line_cda, draw_line_brez_float, draw_line_brez_int,
         draw_line_brez_smoth, draw_line_vu, canvas.create_line)
test_funcs = (cda_test, float_test, int_test, smoth_test, vu_test)

# Координаты начала и конца отрезка
lb1 = Label(coords_frame, text='Координаты начала отрезка')
lb2 = Label(coords_frame, text='Координаты конца отрезка')
lb1.place(x=0, y=5)
lb2.place(x=0, y=50)

btn_draw = Button(coords_frame, text="Построить",
                  font='Calibri 15', 
                  command=lambda: draw(0), width=140, height=25)
btn_draw.place(x=170, y=35, width=100, height=30)

lbx1 = Label(coords_frame, text='X:')
lby1 = Label(coords_frame, text='Y:')
lbx2 = Label(coords_frame, text='X:')
lby2 = Label(coords_frame, text='Y:')
lbx1.place(x=5, y=25)
lby1.place(x=90, y=25)
lbx2.place(x=5, y=75)
lby2.place(x=90, y=75)

fxs = Entry(coords_frame, bg="white")
fys = Entry(coords_frame, bg="white")
fxf = Entry(coords_frame, bg="white")
fyf = Entry(coords_frame, bg="white")

fxs.place(x=30, y=25, width=35)
fys.place(x=115, y=25, width=35)
fxf.place(x=30, y=75, width=35)
fyf.place(x=115, y=75, width=35)

fxs.insert(0, str(CANVAS_WIDTH / 2))
fys.insert(0, str(CANVAS_HEIGHT / 2))
fxf.insert(0, str(CANVAS_WIDTH / 2 + line_r))
fyf.insert(0, str(CANVAS_HEIGHT/2 + line_r))

lb_angle = Label(angle_frame, text="Угол поворота\n(в градусах):")
lb_angle.place(x=2, y=2)

fangle = Entry(angle_frame, bg="white")
fangle.place(x=30, y=40, width=25)
fangle.insert(0, "15")

btn_viz = Button(angle_frame, text="Спектр", command=lambda: draw(1))
btn_viz.place(x=120, y=30, width=120, height=25)

lb_len = Label(comparison_frame, text="Длина отрезка\n(по умолчанию - 100)",
               font='Calibri 15')
lb_len.place(x=75, y=0)

len_line = Entry(comparison_frame, font='Calibri 15', justify='center')
len_line.place(x=0, y=60, width=400)

btn_time = Button(comparison_frame, text="Временной\nанализ",
                  font='Calibri 15', command=lambda: analyze(0))
btn_time.place(x=0, y=90, width=190)

btn_smoth = Button(comparison_frame, text="Сравнение\nступенчатости",
                   font='Calibri 15', command=lambda: analyze(1))
btn_smoth.place(x=220, y=90, width=190)

btn_clean = Button(menu_frame, text="Очистить экран", font='Calibri 15',
                   command=clean)
btn_clean.place(x=0, y=0, width=190)

btn_help = Button(menu_frame, text="Информация", font='Calibri 15',
                  command=show_info)
btn_help.place(x=220, y=0, width=190)


# выбор цветов
line_color = 'black'
bg_color = 'white'

size = 15
white_line = Button(color_frame, bg="white", activebackground="white",
                    command=lambda: set_linecolor('white'))
white_line.place(x=15, y=30, height=size, width=size)
black_line = Button(color_frame, bg="yellow", activebackground="black",
                    command=lambda: set_linecolor("yellow"))
black_line.place(x=30, y=30, height=size, width=size)
red_line = Button(color_frame, bg="orange", activebackground="orange",
                  command=lambda: set_linecolor("orange"))
red_line.place(x=45, y=30, height=size, width=size)
orange_line = Button(color_frame, bg="red", activebackground="red",
                     command=lambda: set_linecolor("red"))
orange_line.place(x=60, y=30, height=size, width=size)
yellow_line = Button(color_frame, bg="purple", activebackground="purple",
                     command=lambda: set_linecolor("purple"))
yellow_line.place(x=75, y=30, height=size, width=size)
green_line = Button(color_frame, bg="darkblue", activebackground="darkblue",
                    command=lambda: set_linecolor("darkblue"))
green_line.place(x=90, y=30, height=size, width=size)
doger_line = Button(color_frame, bg="darkgreen", activebackground="darkgreen",
                    command=lambda: set_linecolor("darkgreen"))
doger_line.place(x=105, y=30, height=size, width=size)
blue_line = Button(color_frame, bg="black", activebackground="black",
                   command=lambda: set_linecolor("black"))
blue_line.place(x=120, y=30, height=size, width=size)

white_bg = Button(color_frame, bg="white", activebackground="white",
                  command=lambda: set_bgcolor("white"))
white_bg.place(x=15, y=110, height=size, width=size)
black_bg = Button(color_frame, bg="yellow", activebackground="yellow",
                  command=lambda: set_bgcolor("yellow"))
black_bg.place(x=30, y=110, height=size, width=size)
red_bg = Button(color_frame, bg="orange", activebackground="orange",
                command=lambda: set_bgcolor("orange"))
red_bg.place(x=45, y=110, height=size, width=size)
orange_bg = Button(color_frame, bg="red", activebackground="red",
                   command=lambda: set_bgcolor("red"))
orange_bg.place(x=60, y=110, height=size, width=size)
yellow_bg = Button(color_frame, bg="purple", activebackground="purple",
                   command=lambda: set_bgcolor("purple"))
yellow_bg.place(x=75, y=110, height=size, width=size)
green_bg = Button(color_frame, bg="darkblue", activebackground="darkblue",
                  command=lambda: set_bgcolor("darkblue"))
green_bg.place(x=90, y=110, height=size, width=size)
dodger_bg = Button(color_frame, bg="darkgreen", activebackground="darkgreen",
                   command=lambda: set_bgcolor("darkgreen"))
dodger_bg.place(x=105, y=110, height=size, width=size)
blue_bg = Button(color_frame, bg="black", activebackground="black",
                 command=lambda: set_bgcolor("black"))
blue_bg.place(x=120, y=110, height=size, width=size)

lb_line = Label(color_frame, text='Цвет отрезка (текущий:          ): ')
lb_line.place(x=2, y=5)

lb_lcolor = Label(color_frame, bg=line_color)
lb_lcolor.place(x=137, y=9, width=24, height=12)

lb_bg = Label(color_frame, text='Цвет фона:')
lb_bg.place(x=2, y=80)

draw_axes()
main_window.mainloop()
