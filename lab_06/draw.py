from tkinter import messagebox
from time import time

from constants import *
from bresenham import bresenham_int

INDEX_POINT = 0
BORDER_COLOR = '#ffc0cb' # ff8000


def clear_canvas(img, figures:list, time_entry, points_listbox, seed_pixel: list):
    global INDEX_POINT

    img.put("#ffffff", to=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))

    seed_pixel[0] = -1
    seed_pixel[1] = -1

    INDEX_POINT = 0

    points_listbox.delete(0, 'end')
    time_entry.delete(0, 'end')

    figures.clear()
    figures.append([[]])

    draw_frame(figures, img)


def draw_pixel(img, x, y, color):
    img.put(color, (x, y))


def draw_line(img, points: list):
    for i in points:
        draw_pixel(img, i[0], i[1], i[2])


def rgb(color: str) -> tuple:
    return int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)


def get_color(color_var):
    col_var = color_var.get()

    if col_var == 0:
        color = "#000001"
    elif col_var == 1:
        color = "#ff0000"
    elif col_var == 2:
        color = "#0000ff"
    elif col_var == 3:
        color = "#3ebd33"
    elif col_var == 4:
        color = "#ffd333"
    else:
        color = "#bd08fc"

    return color


def draw_point(figures: list, img, x_entry, y_entry, points_listbox):
    global INDEX_POINT

    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except:
        messagebox.showerror("Ошибка!",
                             "Координаты точки должны быть целыми числами.")

        return

    color = BORDER_COLOR
    draw_pixel(img, x, y, color)

    figures[-1][-1].append([x, y])

    INDEX_POINT += 1
    info_string = f"{INDEX_POINT}. ({x}, {y})"

    points_listbox.insert('end', info_string)

    if len(figures[-1][-1]) == 2:
        points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
        draw_line(img, points)

        figures[-1][-1].append(points)
        figures[-1].append([figures[-1][-1][1]])


def draw_border(figures: list, img, x, y):    
    color = BORDER_COLOR
    draw_pixel(img, x, y, color)

    figures[-1][-1].append([x, y])

    if len(figures[-1][-1]) == 2:
        points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
        draw_line(img, points)

        figures[-1][-1].append(points)
        figures[-1].append([figures[-1][-1][1]])


def draw_frame(figures: list, img):
    draw_border(figures, img, 0, 0)
    draw_border(figures, img, CANVAS_WIDTH, 0)
    draw_border(figures, img, CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_border(figures, img, 0, CANVAS_HEIGHT)
    click_right(figures, img)


def flood_fill_algorithm(img, canvas, seed_pixel, mark_color, border_color_rgb, delay):
    mark_color_rgb = rgb(mark_color)

    stack = [seed_pixel]

    while len(stack):
        seed_pixel = stack.pop()

        x = seed_pixel[0]
        y = seed_pixel[1]

        draw_pixel(img, x, y, mark_color)

        x_tmp = x
        y_tmp = y

        x += 1

        while img.get(x, y) != border_color_rgb and img.get(x, y) != \
                mark_color_rgb and x < CANVAS_WIDTH:
            draw_pixel(img, x, y, mark_color)
            x += 1

        x_right = x - 1
        x = x_tmp - 1

        while img.get(x, y) != mark_color_rgb and img.get(x, y) != border_color_rgb and x > 0:
            draw_pixel(img, x, y, mark_color)
            x -= 1

        x_left = x + 1

        x = x_left
        y = y_tmp + 1

        while x_left <= x <= x_right:
            flag = False

            while img.get(x, y) != mark_color_rgb and img.get(x, y) != border_color_rgb and x <= x_right:
                flag = True
                x += 1

            if flag:
                if x == x_right and img.get(x, y) != mark_color_rgb and img.get(x, y) != border_color_rgb:
                    stack.append([x, y])
                else:
                    stack.append([x - 1, y])

                flag = False

            x_beg = x
            while (img.get(x, y) == mark_color_rgb or img.get(x, y) == border_color_rgb) and x < x_right:
                x = x + 1

            if x == x_beg:
                x += 1

        x = x_left
        y = y_tmp - 1

        while x_left <= x <= x_right:
            flag = False

            while img.get(x, y) != mark_color_rgb and img.get(x, y) != border_color_rgb and x <= x_right:
                flag = True
                x += 1

            if flag:
                if x == x_right and img.get(x, y) != mark_color_rgb and img.get(x, y) != border_color_rgb:
                    stack.append([x, y])
                else:
                    stack.append([x - 1, y])

                flag = False

            x_beg = x
            while (img.get(x, y) == mark_color_rgb or img.get(x, y) == border_color_rgb) and x < x_right:
                x = x + 1

            if x == x_beg:
                x += 1

        if delay:
            canvas.update()


def fill_figure(figures, img, canvas, color_var, mode_var, time_entry, seed_pixel):
    if len(figures[-1][0]) != 0:
        messagebox.showerror("Ошибка!", "Не все фигуры замкнуты.")

        return

    if seed_pixel == [-1, -1]:
        messagebox.showerror("Ошибка!", "Отсутствует затравка.")

        return

    mark_color = get_color(color_var)
    border_color = rgb(BORDER_COLOR)

    delay = mode_var.get()

    start_time = time()
    flood_fill_algorithm(img, canvas, seed_pixel, mark_color, border_color, delay)
    end_time = time()

    time_str = str(round(end_time - start_time, 2)) + " сек"

    time_entry.delete(0, 'end')
    time_entry.insert(0, time_str)


def click_left(event, figures, img, points_listbox):
    global INDEX_POINT

    x = event.x
    y = event.y

    color = BORDER_COLOR
    draw_pixel(img, x, y, color)

    figures[-1][-1].append([x, y])

    INDEX_POINT += 1
    info_string = f"{INDEX_POINT}. ({x}, {y})"

    points_listbox.insert('end', info_string)

    if len(figures[-1][-1]) == 2:
        points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
        draw_line(img, points)

        figures[-1][-1].append(points)
        figures[-1].append([figures[-1][-1][1]])


def click_right(figures, img):
    if len(figures[-1][-1]) == 0:
        messagebox.showerror("Ошибка!", "Все фигуры замкнуты.")

        return

    if len(figures[-1]) <= 2:
        messagebox.showerror("Ошибка!", "Фигура должна иметь более 1 ребра.")

        return

    point = figures[-1][0][0]
    figures[-1][-1].append(point)

    color = BORDER_COLOR

    points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
    draw_line(img, points)

    figures[-1][-1].append(points)
    figures.append([[]])


def click_wheel(event, seed_pixel, img, color_var, points_listbox):
    x = event.x
    y = event.y

    seed_pixel[0] = x
    seed_pixel[1] = y

    color = get_color(color_var)
    draw_pixel(img, x, y, color)

    info_string = f"Затравка = ({x}, {y})"
    points_listbox.insert('end', info_string)
