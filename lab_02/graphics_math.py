import math


def canvas_clear(canvas_name):
    canvas_name.delete('all')


def draw_line_in_center(x_0: int, y_0: int, x_1: int, y_1: int,
                        color: str, canvas_name):
    canvas_name.create_line(x_0, y_0, x_1, y_1, fill=color)


def draw_line(coordinates: list, canvas_size: list, color: str, canvas_name):
    draw_line_in_center(coordinates[0][0] + canvas_size[0] / 2,
                        -coordinates[0][1] + canvas_size[1] / 2,
                        coordinates[1][0] + canvas_size[0] / 2,
                        -coordinates[1][1] + canvas_size[1] / 2,
                        color, canvas_name)


def draw_axes(canvas_size: list, color: str, canvas_name):
    draw_line_in_center(0, canvas_size[1] / 2, canvas_size[0],
                        canvas_size[1] / 2, color, canvas_name)
    draw_line_in_center(canvas_size[0] / 2, 0, canvas_size[0] / 2,
                        canvas_size[1], color, canvas_name)


def transfer_point(x: float, y: float, d_x: float, d_y: float) -> list:
    x += d_x
    y += d_y

    return [x, y]


def scale_point(x: float, y: float, k_x: float, k_y: float,
                x_c: float, y_c: float) -> list:
    x = k_x * x + (1 - k_x) * x_c
    y = k_y * y + (1 - k_y) * y_c

    return [x, y]


def rotate_point(x: float, y: float, phi: float, x_c: float,
                 y_c: float) -> list:
    teta = phi * math.pi / 180.0

    x_c_tmp = 0
    y_c_tmp = 0

    x_tmp = x - x_c_tmp
    y_tmp = y - y_c_tmp

    x_res = x_tmp * math.cos(teta) - y_tmp * math.sin(teta)
    y_res = x_tmp * math.sin(teta) + y_tmp * math.cos(teta)

    return [x_res, y_res]


def poly_oval(x0, y0, x1, y1):
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0

    xc = x0 + a
    yc = y0 + b

    point_list = []

    steps = 20

    for i in range(steps):
        theta = (math.pi * 2) * (float(i) / steps)

        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)

        point_list.append(round(x1 + xc))
        point_list.append(round(y1 + yc))

    return point_list
