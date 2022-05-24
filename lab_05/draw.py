import constants as const
import time

from bresenham import *
from tkinter import *
from tkinter import messagebox

index_point = 0


def clear_canvas(img, canvas, figures, p_min, p_max, time_entry, points_listbox):
    global index_point

    img.put("#FFFFFF", to=(0, 0, const.CANVAS_WIDTH, const.CANVAS_HEIGHT))

    p_min[0] = const.CANVAS_WIDTH
    p_min[1] = const.CANVAS_HEIGHT
    p_max[0] = 0
    p_max[1] = 0

    index_point = 0
    points_listbox.delete(0, END)
    time_entry.delete(0, END)
    figures.clear()
    figures.append([[]])


def draw_line(img, points):
    for i in points:
        set_pixel(img, i[0], i[1], i[2])


def rgb(color):
    return int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)


def get_color(color_var):
    col_var = color_var.get()

    if col_var == 0:
        color = "#bd08fc"
    elif col_var == 1:
        color = "#000000"
    elif col_var == 2:
        color = "#ff0000"
    elif col_var == 3:
        color = "#0000ff"
    elif col_var == 4:
        color = "#3ebd33"
    else:
        color = "#ffd333"

    return color


def max_min_point(x, y, p_min, p_max):
    if x > p_max[0]:
        p_max[0] = x
    if x < p_min[0]:
        p_min[0] = x
    if y > p_max[1]:
        p_max[1] = y
    if y < p_min[1]:
        p_min[1] = y


def draw_point(figures, img, color_var, x_entry, y_entry, p_min, p_max, points_listbox):
    global index_point

    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except:
        messagebox.showerror("Ошибка!",
                             "Координаты точки должны быть целыми числами.")
        return

    max_min_point(x, y, p_min, p_max)

    color = get_color(color_var)
    set_pixel(img, x, y, color)

    figures[-1][-1].append([x, y])

    index_point += 1
    pstr = "%d. (%d, %d)" % (index_point, x, y)
    points_listbox.insert(END, pstr)

    if len(figures[-1][-1]) == 2:
        points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
        draw_line(img, points)

        figures[-1][-1].append(points)
        figures[-1].append([figures[-1][-1][1]])


def draw_borders(img, figures):
    for fig in figures:
        for line in fig:
            if len(line) != 0:
                draw_line(img, line[2])


def fill_figure(figures, img, canvas, color_var, p_min, p_max, mode_var, time_entry):
    if len(figures[-1][0]) != 0:
        messagebox.showerror("Ошибка!", "Не все фигуры замкнуты.")
        return

    mark_color = "#ff8000"
    bg_color = "#ffffff"
    figure_color = get_color(color_var)

    delay = mode_var.get()

    start_time = time.time()
    method_with_flag(figures, img, canvas, mark_color, bg_color, figure_color, p_min, p_max, delay)
    end_time = time.time()

    draw_borders(img, figures)

    time_str = str(round(end_time - start_time, 2)) + " сек"
    time_entry.delete(0, END)
    time_entry.insert(0, time_str)


def mark_desired_pixels(img, figures, mark_color):
    mark_color_rgb = rgb(mark_color)

    for fig in figures:
        for line in fig:
            if len(line) == 0 or line[1][1] == line[0][1]:
                continue

            if line[1][1] > line[0][1]:
                y_max = line[1][1]
                y_min = line[0][1]
            else:
                y_max = line[0][1]
                y_min = line[1][1]

            dx = line[1][0] - line[0][0]
            dy = line[1][1] - line[0][1]

            y = y_min
            while y < y_max:
                x = dx / dy * (y - line[0][1]) + line[0][0]

                if img.get(int(x) + 1, y) == mark_color_rgb:
                    set_pixel(img, int(x) + 2, y, mark_color)
                else:
                    set_pixel(img, int(x) + 1, y, mark_color)

                y += 1


def method_with_flag(figures, img, canvas, mark_color, bg_color, figure_color, p_min, p_max, delay):
    mark_desired_pixels(img, figures, mark_color)
    mark_color_rgb = rgb(mark_color)

    flag = False

    for y in range(p_max[1], p_min[1] - 1, -1):
        for x in range(p_min[0], p_max[0] + 3):

            if img.get(x, y) == mark_color_rgb:
                flag = not flag

            if flag:
                set_pixel(img, x, y, figure_color)
            else:
                set_pixel(img, x, y, bg_color)

        if delay:
            canvas.update()


def click_left(event, figures, img, color_var, p_min, p_max, points_listbox):
    global index_point

    x = event.x
    y = event.y

    max_min_point(x, y, p_min, p_max)

    color = get_color(color_var)
    set_pixel(img, x, y, color)

    figures[-1][-1].append([x, y])

    index_point += 1
    pstr = f"{index_point}. ({x}, {y})"
    points_listbox.insert(END, pstr)

    if len(figures[-1][-1]) == 2:
        points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
        draw_line(img, points)

        figures[-1][-1].append(points)
        figures[-1].append([figures[-1][-1][1]])


def click_right(event, figures, img, color_var):
    if len(figures[-1][-1]) == 0:
        messagebox.showerror("Ошибка!", "Незамкнутых фигур нет.")
        return

    if len(figures[-1]) <= 2:
        messagebox.showerror("Ошибка!", "Фигура должна иметь больше 1 ребра.")
        return

    point = figures[-1][0][0]
    figures[-1][-1].append(point)

    color = get_color(color_var)

    points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
    draw_line(img, points)

    figures[-1][-1].append(points)
    figures.append([[]])
