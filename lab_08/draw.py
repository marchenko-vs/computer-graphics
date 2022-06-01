import cyrus_beck_algorithm as cba
import itertools

from tkinter import messagebox


def clear_canvas(canvas, lines, clipping_window):
    canvas.delete("all")

    lines.clear()
    lines.append([])

    clipping_window.clear()


def clear_clipping_window(canvas, lines, clipping_window):
    canvas.delete("all")

    draw_lines(canvas, lines)
    clipping_window.clear()


def draw_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill=color)


def draw_lines(canvas, lines):
    for line in lines:
        if len(line) == 3:
            canvas.create_line(line[0], line[1], fill=line[2])


def get_color(color_var):
    color = ""
    col_var = color_var.get()

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


def draw_line(lines, canvas, color_var, xb_entry, yb_entry, xe_entry, ye_entry):
    if len(lines[-1]) != 0:
        messagebox.showerror("Ошибка!",
                             "Предыдущий отрезок не был достроен.")
        return

    try:
        xb = int(xb_entry.get())
        yb = int(yb_entry.get())
        xe = int(xe_entry.get())
        ye = int(ye_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка!",
                             "Координаты начала и конца отрезка должны быть целыми числами.")
        return

    color = get_color(color_var)

    canvas.create_line([xb, yb], [xe, ye], fill=color)

    lines[-1].append([xb, yb])
    lines[-1].append([xe, ye])
    lines[-1].append(color)
    lines.append([])


def clipping_window_add_vertex(lines, clipping_window, canvas, color_var, x_clip_entry, y_clip_entry):
    try:
        x = int(x_clip_entry.get())
        y = int(y_clip_entry.get())
    except ValueError:
        messagebox.showerror("Ошибка!",
                             "Координаты вершин отсекателя должны быть целыми числами.")
        return

    if len(clipping_window) > 3 and clipping_window[0] == clipping_window[-1]:
        clear_clipping_window(canvas, lines, clipping_window)

    if (len(clipping_window) > 0 and clipping_window[-1][0] == x and
            clipping_window[-1][1] == y):
        return

    color = get_color(color_var)
    draw_pixel(canvas, x, y, color)

    clipping_window.append([x, y])

    if len(clipping_window) >= 2:
        canvas.create_line(clipping_window[-2], clipping_window[-1], fill=color)


def find_first_dot(clipping_window):
    max_y = clipping_window[0][1]
    i_max = 0

    for i in range(len(clipping_window)):
        if clipping_window[i][1] > max_y:
            max_y = clipping_window[i][1]
            i_max = i

    clipping_window.pop()

    for i in range(i_max):
        clipping_window.append(clipping_window.pop(0))

    clipping_window.append(clipping_window[0])

    if cross_product(cba.get_vector(clipping_window[1], clipping_window[2]),
                     cba.get_vector(clipping_window[0], clipping_window[1])) < 0:
        clipping_window.reverse()


def line_coefficients(x_0, y_0, x_1, y_1):
    a = y_0 - y_1
    b = x_1 - x_0
    c = x_0 * y_1 - x_1 * y_0

    return a, b, c


def get_lines_intersection(a_0, b_0, c_0, a_1, b_1, c_1):
    opr = a_0 * b_1 - a_1 * b_0
    opr1 = (-c_0) * b_1 - b_0 * (-c_1)
    opr2 = a_0 * (-c_1) - (-c_0) * a_1

    if opr == 0:
        return -1, -1  # прямые параллельны

    x = opr1 / opr
    y = opr2 / opr

    return x, y


def is_coordinate_between(left_coordinate, right_coordinate, dot_coordinate):
    return min(left_coordinate, right_coordinate) <= dot_coordinate <= max(left_coordinate, right_coordinate)


def is_dot_between(dot_left, dot_right, dot_intersection):
    return is_coordinate_between(dot_left[0], dot_right[0], dot_intersection[0]) and \
           is_coordinate_between(dot_left[1], dot_right[1], dot_intersection[1])


def are_edges_linked(line_1, line_2):
    if (line_1[0][0] == line_2[0][0] and line_1[0][1] == line_2[0][1]) or \
            (line_1[1][0] == line_2[1][0] and line_1[1][1] == line_2[1][1]) or \
            (line_1[0][0] == line_2[1][0] and line_1[0][1] == line_2[1][1]) or \
            (line_1[1][0] == line_2[0][0] and line_1[1][1] == line_2[0][1]):
        return True

    return False


def extra_polygon_check(clipping_window):
    """есть ли пересечения между несоседними ребрами"""
    clipping_lines = []

    for i in range(len(clipping_window) - 1):
        clipping_lines.append([clipping_window[i], clipping_window[i + 1]])

    lines_combinations = list(itertools.combinations(clipping_lines, 2))

    for i in range(len(lines_combinations)):
        line_1 = lines_combinations[i][0]
        line_2 = lines_combinations[i][1]

        if are_edges_linked(line_1, line_2):
            continue

        a1, b1, c1 = line_coefficients(line_1[0][0], line_1[0][1], line_1[1][0], line_1[1][1])
        a2, b2, c2 = line_coefficients(line_2[0][0], line_2[0][1], line_2[1][0], line_2[1][1])

        dot_intersection = get_lines_intersection(a1, b1, c1, a2, b2, c2)

        if is_dot_between(line_1[0], line_1[1], dot_intersection) and \
            is_dot_between(line_2[0], line_2[1], dot_intersection):
            return True

    return False


def cross_product(vector_1, vector_2):
    return vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]


def is_polygon_convex(clipping_window):
    if cross_product(cba.get_vector(clipping_window[1], clipping_window[2]),
                     cba.get_vector(clipping_window[0], clipping_window[1])) > 0:
        flag = 1  # по часовой стрелке
    else:
        flag = -1

    for i in range(3, len(clipping_window)):
        if flag * cross_product(cba.get_vector(clipping_window[i - 1], clipping_window[i]),
                                cba.get_vector(clipping_window[i - 2], clipping_window[i - 1])) < 0:
            return False

    return True


def clip(clipping_window, lines, canvas, color_clipping_var, color_result_var):
    if len(clipping_window) < 4:
        messagebox.showerror("Ошибка!", "Отсекатель отсутствует.")
        return

    if clipping_window[0] != clipping_window[-1]:
        messagebox.showerror("Ошибка!", "Отсекатель не замкнут.")
        return

    if not is_polygon_convex(clipping_window):
        messagebox.showerror("Ошибка!", "Отсекатель должен быть выпуклым многоугольником.")
        return

    if extra_polygon_check(clipping_window[:]):
        messagebox.showerror("Ошибка!", "Отсекатель должен быть многоугольником.")
        return

    clipping_color = get_color(color_clipping_var)
    result_color = get_color(color_result_var)

    canvas.create_polygon(clipping_window, outline=clipping_color, fill="white")
    find_first_dot(clipping_window)

    for line in lines:
        if len(line) == 3:
            cba.cyrus_beck_algorithm(line, clipping_window, result_color, canvas)


def click_left(event, lines, canvas, color_var):
    x = event.x
    y = event.y

    color = get_color(color_var)
    draw_pixel(canvas, x, y, color)

    lines[-1].append([x, y])

    if len(lines[-1]) == 2:
        canvas.create_line(lines[-1][0], lines[-1][1], fill=color)

        lines[-1].append(color)
        lines.append([])


def click_right(event, lines, cutter_figure, canvas, color_var):
    if len(cutter_figure) > 3 and cutter_figure[0] == cutter_figure[-1]:
        clear_clipping_window(canvas, lines, cutter_figure)

    x = event.x
    y = event.y

    if (len(cutter_figure) > 0 and cutter_figure[-1][0] == x and
            cutter_figure[-1][1] == y):
        return

    color = get_color(color_var)
    draw_pixel(canvas, x, y, color)

    cutter_figure.append([x, y])

    if len(cutter_figure) >= 2:
        canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill=color)


def click_wheel(cutter_figure, canvas, color_var):
    if len(cutter_figure) < 3:
        messagebox.showerror("Ошибка!",
                             "Отсекатель должен иметь более 2-х вершин.")
        return

    if cutter_figure[0] == cutter_figure[-1]:
        return

    color = get_color(color_var)
    cutter_figure.append(cutter_figure[0])

    canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill=color)
