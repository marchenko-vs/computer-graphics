import constants as const

from math import pi, sin, cos
from numpy import arange
from tkinter import messagebox

default_scale = 50
transformation_matrix = list()


def clear_canvas(canvas):
    canvas.delete("all")


def set_transformation_matrix():
    global transformation_matrix

    transformation_matrix.clear()

    for i in range(4):
        tmp_arr = []

        for j in range(4):
            tmp_arr.append(int(i == j))

        transformation_matrix.append(tmp_arr)


def choose_color(color_var):
    col_var = color_var.get()
    color = ''

    match col_var:
        case 0:
            color = "#000000"
        case 1:
            color = "#ff0000"
        case 2:
            color = "#0000ff"
        case 3:
            color = "#3ebd33"
        case 4:
            color = "#ffa600"
        case 5:
            color = "#bd08fc"

    return color


def choose_function(function_var):
    function = None

    match function_var:
        case 0:
            function = lambda x, z: sin(x) * cos(z)
        case 1:
            function = lambda x, z: sin(cos(x)) * sin(z)
        case 2:
            function = lambda x, z: cos(x) * z / 4
        case 3:
            function = lambda x, z: cos(x) * cos(sin(z))

    return function


def scan_limits(x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry):
    try:
        x_0 = float(x_0_entry.get())
        x_1 = float(x_1_entry.get())
        x_2 = float(x_2_entry.get())

        x_limits = [x_0, x_1, x_2]

        z_0 = float(z_0_entry.get())
        z_1 = float(z_1_entry.get())
        z_2 = float(z_2_entry.get())

        z_limits = [z_0, z_1, z_2]

        return x_limits, z_limits
    except ValueError:
        return None, None


def rotate_matrix(matrix):
    global transformation_matrix

    res_matrix = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                res_matrix[i][j] += transformation_matrix[i][k] * matrix[k][j]

    transformation_matrix = res_matrix


def rotate_x(x_spin_entry, canvas, color_var, func_var,
             x_0_entry, x_1_entry, x_2_entry,
             z_0_entry, z_1_entry, z_2_entry):
    try:
        angle = float(x_spin_entry.get()) / 180 * pi
    except ValueError:
        messagebox.showerror("Ошибка!", "Угол поворота должен быть числом.")
        return

    if len(transformation_matrix) == 0:
        messagebox.showerror("Ошибка!", "График не задан.")
        return

    rotating_matrix = [[1, 0, 0, 0],
                       [0, cos(angle), sin(angle), 0],
                       [0, -sin(angle), cos(angle), 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    build_function(canvas, color_var, func_var,
                   x_0_entry, x_1_entry, x_2_entry,
                   z_0_entry, z_1_entry, z_2_entry)


def rotate_y(y_spin_entry, canvas, color_var, func_var,
             x_0_entry, x_1_entry, x_2_entry,
             z_0_entry, z_1_entry, z_2_entry):
    try:
        angle = float(y_spin_entry.get()) / 180 * pi
    except ValueError:
        messagebox.showerror("Ошибка!", "Угол поворота должен быть числом.")
        return

    if len(transformation_matrix) == 0:
        messagebox.showerror("Ошибка!", "График не задан.")
        return

    rotating_matrix = [[cos(angle), 0, -sin(angle), 0],
                       [0, 1, 0, 0],
                       [sin(angle), 0, cos(angle), 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    build_function(canvas, color_var, func_var,
                   x_0_entry, x_1_entry, x_2_entry,
                   z_0_entry, z_1_entry, z_2_entry)


def rotate_z(z_spin_entry, canvas, color_var, func_var,
             x_0_entry, x_1_entry, x_2_entry,
             z_0_entry, z_1_entry, z_2_entry):
    try:
        angle = float(z_spin_entry.get()) / 180 * pi
    except ValueError:
        messagebox.showerror("Ошибка!", "Угол поворота должен быть числом.")
        return

    if len(transformation_matrix) == 0:
        messagebox.showerror("Ошибка!", "График не задан.")
        return

    rotating_matrix = [[cos(angle), sin(angle), 0, 0],
                       [-sin(angle), cos(angle), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    build_function(canvas, color_var, func_var,
                   x_0_entry, x_1_entry, x_2_entry,
                   z_0_entry, z_1_entry, z_2_entry)


def scale_function(scale_entry, canvas, color_var, func_var,
                   x_0_entry, x_1_entry, x_2_entry,
                   z_0_entry, z_1_entry, z_2_entry):
    try:
        scale_param = float(scale_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка!", "Коэффициент масштабирования должен быть числом.")
        return

    if len(transformation_matrix) == 0:
        messagebox.showerror("Ошибка!", "График не задан.")
        return

    build_function(canvas, color_var, func_var,
                   x_0_entry, x_1_entry, x_2_entry,
                   z_0_entry, z_1_entry, z_2_entry,
                   False, scale_param)


def transfer_dot(dot, scale_param):
    dot.append(1)

    res_dot = [0, 0, 0, 0]

    for i in range(4):
        for j in range(4):
            res_dot[i] += dot[j] * transformation_matrix[j][i]

    for i in range(3):
        res_dot[i] *= scale_param

    res_dot[0] += const.CANVAS_WIDTH // 2
    res_dot[1] += const.CANVAS_HEIGHT // 2

    return res_dot[:3]


def is_visible(dot):
    return (0 <= dot[0] <= const.CANVAS_WIDTH) and \
           (0 <= dot[1] <= const.CANVAS_HEIGHT)


def draw_pixel(x, y, canvas, color_var):
    color = choose_color(color_var)

    canvas.create_line(x, y, x + 1, y + 1, fill=color)


def draw_dot(x, y, high_horizon, low_horizon, canvas, color_var):
    if not is_visible([x, y]):
        return False

    x = int(x)
    y = int(y)

    if y > high_horizon[x]:
        high_horizon[x] = y
        draw_pixel(x, y, canvas, color_var)

    elif y < low_horizon[x]:
        low_horizon[x] = y
        draw_pixel(x, y, canvas, color_var)

    return True


def draw_horizon_part(dot1, dot2, high_horizon, low_horizon, canvas, color_var):
    if dot1[0] > dot2[0]:
        dot1, dot2 = dot2, dot1

    dx = dot2[0] - dot1[0]
    dy = dot2[1] - dot1[1]

    if dx > dy:
        l = dx
    else:
        l = dy

    dx /= l
    dy /= l

    x = dot1[0]
    y = dot1[1]

    for _ in range(int(l) + 1):
        if not draw_dot(round(x), y, high_horizon, low_horizon, canvas, color_var):
            return

        x += dx
        y += dy


def draw_horizon(function, high_horizon, low_horizon, limits, z, scale_param, canvas, color_var):
    f = lambda x: function(x, z)

    prev = None

    for x in arange(limits[0], limits[1] + limits[2], limits[2]):
        cur = transfer_dot([x, f(x), z], scale_param)

        if prev:
            draw_horizon_part(prev, cur, high_horizon, low_horizon, canvas, color_var)

        prev = cur


def draw_horizon_limits(f, x_limits, z_limits, scale_param, canvas, color_var):
    color = choose_color(color_var)

    for z in arange(z_limits[0], z_limits[1] + z_limits[2], z_limits[2]):
        dot1 = transfer_dot([x_limits[0], f(x_limits[0], z), z], scale_param)
        dot2 = transfer_dot([x_limits[0], f(x_limits[0], z + x_limits[2]), z + x_limits[2]], scale_param)

        canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill=color)

        dot1 = transfer_dot([x_limits[1], f(x_limits[1], z), z], scale_param)
        dot2 = transfer_dot([x_limits[1], f(x_limits[1], z + x_limits[2]), z + x_limits[2]], scale_param)

        canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill=color)


def build_function(canvas, color_var, func_var,
                   x_0_entry, x_1_entry, x_2_entry,
                   z_0_entry, z_1_entry, z_2_entry,
                   new_graph=False, scale_param=default_scale):
    clear_canvas(canvas)

    if new_graph:
        set_transformation_matrix()

    f = choose_function(func_var.get())
    x_limits, z_limits = scan_limits(x_0_entry, x_1_entry, x_2_entry,
                                     z_0_entry, z_1_entry, z_2_entry)

    if x_limits is None or z_limits is None:
        messagebox.showerror("Ошибка!", "Пределы должны быть числами.")
        return

    high_horizon = [0 for _ in range(const.CANVAS_WIDTH + 1)]
    low_horizon = [const.CANVAS_HEIGHT for _ in range(const.CANVAS_WIDTH + 1)]

    #  Горизонт
    for z in arange(z_limits[0], z_limits[1] + z_limits[2], z_limits[2]):
        draw_horizon(f, high_horizon, low_horizon, x_limits, z, scale_param, canvas, color_var)

    # Границы горизонта
    draw_horizon_limits(f, x_limits, z_limits, scale_param, canvas, color_var)
