from tkinter import messagebox
from cyrus_beck import check_polygon, cyrus_beck_algorithm, get_vector, vector_mul
from itertools import combinations


def clear_canvas(canvas, lines, cutter_figure):
    canvas.delete("all")

    lines.clear()
    lines.append([])

    cutter_figure.clear()


def clear_cutter_figure(canvas, lines, cutter_figure):
    canvas.delete("all")

    draw_lines(canvas, lines)
    cutter_figure.clear()


def set_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill=color)


def draw_lines(canvas, lines):
    for line in lines:
        if len(line) == 3:
            canvas.create_line(line[0], line[1], fill=line[2])


def get_color(color_var):
    col_var = color_var.get()

    if col_var == 0:
        color = "#000000"
    elif col_var == 1:
        color = "#ff0000"
    elif col_var == 2:
        color = "#0000ff"
    elif col_var == 3:
        color = "#3ebd33"
    elif col_var == 4:
        color = "#ffa600"
    else:
        color = "#bd08fc"

    return color


def click_left(event, lines, canvas, color_var):
    x = event.x
    y = event.y

    color = get_color(color_var)
    set_pixel(canvas, x, y, color)

    lines[-1].append([x, y])

    if len(lines[-1]) == 2:
        canvas.create_line(lines[-1][0], lines[-1][1], fill=color)

        lines[-1].append(color)
        lines.append([])


def click_right(event, lines, cutter_figure, canvas, color_var):
    if (len(cutter_figure) > 3 and cutter_figure[0] == cutter_figure[-1]):
        clear_cutter_figure(canvas, lines, cutter_figure)

    x = event.x
    y = event.y

    if (len(cutter_figure) > 0 and cutter_figure[-1][0] == x and
            cutter_figure[-1][1] == y):
        return

    color = get_color(color_var)
    set_pixel(canvas, x, y, color)

    cutter_figure.append([x, y])

    if len(cutter_figure) >= 2:
        canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill=color)


def click_centre(cutter_figure, canvas, color_var):
    if len(cutter_figure) < 3:
        messagebox.showerror("Ошибка!",
                             "Отсекатель должен иметь более 2-х вершин.")
        return

    if cutter_figure[0] == cutter_figure[-1]:
        return

    color = get_color(color_var)
    cutter_figure.append(cutter_figure[0])

    canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill=color)


def add_line(lines, canvas, color_var, xb_entry, yb_entry, xe_entry, ye_entry):
    if len(lines[-1]) != 0:
        messagebox.showerror("Ошибка!",
                             "Предыдущий отрезок не был достроен.")
        return

    try:
        xb = int(xb_entry.get())
        yb = int(yb_entry.get())
        xe = int(xe_entry.get())
        ye = int(ye_entry.get())
    except:
        messagebox.showerror("Ошибка!",
                             "Координаты начала и конца отрезка должны быть целыми числами.")
        return

    color = get_color(color_var)

    canvas.create_line([xb, yb], [xe, ye], fill=color)

    lines[-1].append([xb, yb])
    lines[-1].append([xe, ye])
    lines[-1].append(color)
    lines.append([])


def add_vertex_figure(lines, cutter_figure, canvas, color_var, x_cut_entry, y_cut_entry):
    try:
        x = int(x_cut_entry.get())
        y = int(y_cut_entry.get())
    except:
        messagebox.showerror("Ошибка!",
                             "Координаты вершин отсекателя должны быть целыми числами.")
        return

    if (len(cutter_figure) > 3 and cutter_figure[0] == cutter_figure[-1]):
        clear_cutter_figure(canvas, lines, cutter_figure)

    color = get_color(color_var)
    set_pixel(canvas, x, y, color)

    cutter_figure.append([x, y])

    if len(cutter_figure) >= 2:
        canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill=color)


def find_starting_dot(cutter_figure):
    max_y = cutter_figure[0][1]
    i_max = 0

    for i in range(len(cutter_figure)):
        if cutter_figure[i][1] > max_y:
            max_y = cutter_figure[i][1]
            i_max = i

    cutter_figure.pop()

    for i in range(i_max):
        cutter_figure.append(cutter_figure.pop(0))

    cutter_figure.append(cutter_figure[0])

    if vector_mul(get_vector(cutter_figure[1], cutter_figure[2]),
                  get_vector(cutter_figure[0], cutter_figure[1])) < 0:
        cutter_figure.reverse()


def line_coefficients(x1, y1, x2, y2):
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1

    return a, b, c


def solve_lines_intersection(a1, b1, c1, a2, b2, c2):
    opr = a1 * b2 - a2 * b1
    opr1 = (-c1) * b2 - b1 * (-c2)
    opr2 = a1 * (-c2) - (-c1) * a2

    if opr == 0:
        return -1, -1  # прямые параллельны

    x = opr1 / opr
    y = opr2 / opr

    return x, y


def is_coord_between(left_coord, right_coord, dot_coord):
    return min(left_coord, right_coord) <= dot_coord <= max(left_coord, right_coord)


def is_dot_between(dot_left, dot_right, dot_intersection):
    return is_coord_between(dot_left[0], dot_right[0], dot_intersection[0]) and \
           is_coord_between(dot_left[1], dot_right[1], dot_intersection[1])


def are_connected_sides(line1, line2):
    if (line1[0][0] == line2[0][0] and line1[0][1] == line2[0][1]) or \
            (line1[1][0] == line2[1][0] and line1[1][1] == line2[1][1]) or \
            (line1[0][0] == line2[1][0] and line1[0][1] == line2[1][1]) or \
            (line1[1][0] == line2[0][0] and line1[1][1] == line2[0][1]):
        return True

    return False


def extra_check_polygon(cutter_figure):
    # есть ли пересечения между несоседними сторонами
    cutter_lines = []

    for i in range(len(cutter_figure) - 1):
        cutter_lines.append([cutter_figure[i], cutter_figure[i + 1]])

    combs_lines = list(combinations(cutter_lines, 2))  # все возможные комбинации сторон

    for i in range(len(combs_lines)):
        line1 = combs_lines[i][0]
        line2 = combs_lines[i][1]

        if are_connected_sides(line1, line2):
            continue

        a1, b1, c1 = line_coefficients(line1[0][0], line1[0][1], line1[1][0], line1[1][1])
        a2, b2, c2 = line_coefficients(line2[0][0], line2[0][1], line2[1][0], line2[1][1])

        dot_intersection = solve_lines_intersection(a1, b1, c1, a2, b2, c2)

        if is_dot_between(line1[0], line1[1], dot_intersection) and \
                is_dot_between(line2[0], line2[1], dot_intersection):
            return True

    return False


def cut_off(cutter_figure, lines, canvas, color_cut_var, color_res_var):
    if len(cutter_figure) < 4:
        messagebox.showerror("Ошибка!", "Отсутствует отсекатель.")
        return

    if cutter_figure[0] != cutter_figure[-1]:
        messagebox.showerror("Ошибка!", "Отсекатель не замкнут.")
        return

    if not check_polygon(cutter_figure):
        messagebox.showerror("Ошибка!", "Отсекатель должен быть выпуклым многоугольником.")
        return

    if extra_check_polygon(cutter_figure[:]):
        messagebox.showerror("Ошибка!", "Отсекатель должен быть многоугольником.")
        return

    cut_color = get_color(color_cut_var)
    res_color = get_color(color_res_var)

    canvas.create_polygon(cutter_figure, outline=cut_color, fill="white")
    find_starting_dot(cutter_figure)

    for line in lines:
        if (len(line) == 3):
            cyrus_beck_algorithm(line, cutter_figure, res_color, canvas)
