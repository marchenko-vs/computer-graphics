import math
# import numpy as np
# import matplotlib.pyplot as plt


EPS = 1e-4


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


def poly_oval(x0, y0, x1, y1, rotation=0):
    rotation = -rotation * math.pi / 180.0

    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0

    xc = x0 + a
    yc = y0 + b

    point_list = []

    steps = 100

    for i in range(steps):
        theta = (math.pi * 2) * (float(i) / steps)

        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)

        x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
        y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))

    return point_list

# def function_circle(x: float, radius: float) -> float:
#     y = math.sqrt(radius ** 2 - x ** 2)
#
#     return y, -y
#
#
# def function_parabola(c: float, d: float, x: float) -> float:
#     y = c - (0.2 * x - d) ** 2
#
#     return y
#
#
# def draw_circle(canvas_size: list, radius: float, canvas_name, begin: float,
#                 end: float, outline: str, width: int):
#     pcur = begin
#
#     while pcur < end:
#         y1, y2 = function_circle(pcur, radius)
#         canvas_name.create_oval(pcur + canvas_size[2] / 2,
#                                 y1 + canvas_size[3] / 2,
#                                 pcur + 1 + canvas_size[2] / 2,
#                                 y1 + 1 + canvas_size[3] / 2)
#         pcur += 1
#
#
# def draw_parabola(canvas_size: list, canvas_name, c: float, d: float, begin: float,
#                 end: float, outline: str, width: int):
#     pcur = begin
#
#     while pcur < end:
#         y = function_parabola(c, d, pcur)
#         canvas_name.create_oval(pcur + canvas_size[2] / 2,
#                                 -y + canvas_size[3] / 2,
#                                 pcur + 1 + canvas_size[2] / 2,
#                                 -y + 1 + canvas_size[3] / 2)
#         pcur += 0.1
#
#
# def draw_circle_2(canvas_size: list, radius: float, canvas_name, begin: float,
#                 end: float, outline: str, width: int):
#     pcur = begin
#
#     while pcur < end:
#         y1, y2 = function_circle(pcur, radius)
#         canvas_name.create_oval(3 * pcur + canvas_size[2] / 2,
#                                 3 * y1 + canvas_size[3] / 2,
#                                 3 * pcur + 1 + canvas_size[2] / 2,
#                                 3 * y1 + 1 + canvas_size[3] / 2)
#         pcur += 1
#
#
# def draw_parabola_2(canvas_size: list, canvas_name, c: float, d: float, begin: float,
#                 end: float, outline: str, width: int):
#     pcur = begin
#
#     while pcur < end:
#         y = function_parabola(c, d, pcur)
#         canvas_name.create_oval(3 * pcur + canvas_size[2] / 2,
#                                 3 * -y + canvas_size[3] / 2,
#                                 3 * pcur + 1 + canvas_size[2] / 2,
#                                 3 * -y + 1 + canvas_size[3] / 2)
#         pcur += 0.1
#
#
# def draw_axes(canvas_size: list, canvas_name, fill: str = 'black',
#               width: int = 1):
#     canvas_name.create_line(0, canvas_size[3] / 2, canvas_size[2],
#                             canvas_size[3] / 2, fill=fill, width=width)
#     canvas_name.create_line(canvas_size[2] / 2, 0, canvas_size[2] / 2,
#                             canvas_size[3], fill=fill, width=width)
#
#
# def draw(canvas_size, canvas_name):
#     draw_axes(canvas_size, canvas_name)
#     r = 100
#
#     x = list(np.arange(-r, r, 0.01))
#     x.append(r)
#     x = np.array(x)
#     circle_pos = []
#     circle_neg = []
#     parabola = []
#
#     for i in x:
#         y = function_circle(i, r)
#         circle_pos.append(y[0])
#         circle_neg.append(y[1])
#
#         parabola.append(function_parabola(33.6, -0.8, i))
#
#     circle_pos = np.array(circle_pos)
#     circle_neg = np.array(circle_neg)
#
#     plt.plot(x, circle_pos, '-')
#     plt.plot(x, circle_neg, '-')
#     plt.plot(x, parabola, '-')
#
#     idx_1 = np.argwhere(np.diff(np.sign(circle_pos - parabola))).flatten()
#     idx_2 = np.argwhere(np.diff(np.sign(circle_neg - parabola))).flatten()
#
#     plt.plot(x[idx_1], circle_pos[idx_1], 'ro')
#     plt.plot(x[idx_2], circle_neg[idx_2], 'ro')
#     plt.show()
#
#     draw_circle(canvas_size, r, canvas_name, float(x[idx_2][0]),
#                 float(x[idx_2][1]), 'red', 1)
#
#     draw_parabola(canvas_size, canvas_name, 33.6, -0.8, float(x[idx_2][0]),
#                 float(x[idx_2][1]), 'red', 1)
#
#     draw_circle_2(canvas_size, r, canvas_name, float(x[idx_2][0]),
#                 float(x[idx_2][1]), 'red', 1)
#
#     draw_parabola_2(canvas_size, canvas_name, 33.6, -0.8, float(x[idx_2][0]),
#                   float(x[idx_2][1]), 'red', 1)
