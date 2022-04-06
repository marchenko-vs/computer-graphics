import math
import numpy as np

from constants import *


def on_one_line(coordinates: list) -> bool:
    result = True

    if abs((coordinates[1][1] - coordinates[0][1]) *
           (coordinates[2][0] - coordinates[0][0]) -
           (coordinates[2][1] - coordinates[0][1]) *
           (coordinates[1][0] - coordinates[0][0])) > EPS:
        result = False

    return result


def circle_in_circle(center_coordinate_1: list, radius_1: float,
                     center_coordinate_2: list, radius_2: float) -> bool:
    result = False

    if (radius_1 + math.sqrt((center_coordinate_1[0] - center_coordinate_2[0]) *
                             (center_coordinate_1[0] - center_coordinate_2[0]) +
                             (center_coordinate_1[1] - center_coordinate_2[1]) *
                             (center_coordinate_1[1] -
                              center_coordinate_2[1]))) <= radius_2:
        result = True

    return result


def get_circle_center(coordinates: list) -> list:
    x_12 = coordinates[0][0] - coordinates[1][0]
    x_23 = coordinates[1][0] - coordinates[2][0]
    x_31 = coordinates[2][0] - coordinates[0][0]

    y_12 = coordinates[0][1] - coordinates[1][1]
    y_23 = coordinates[1][1] - coordinates[2][1]
    y_31 = coordinates[2][1] - coordinates[0][1]

    z_1 = coordinates[0][0] * coordinates[0][0] + \
          coordinates[0][1] * coordinates[0][1]
    z_2 = coordinates[1][0] * coordinates[1][0] + \
          coordinates[1][1] * coordinates[1][1]
    z_3 = coordinates[2][0] * coordinates[2][0] + \
          coordinates[2][1] * coordinates[2][1]

    a = - ((y_12 * z_3 + y_23 * z_1 + y_31 * z_2) /
           (2 * (x_12 * y_31 - y_12 * x_31)))
    b = (x_12 * z_3 + x_23 * z_1 + x_31 * z_2) / \
        (2 * (x_12 * y_31 - y_12 * x_31))

    return [a, b]


def get_circle_radius(center_coordinate: list,
                      circle_coordinate: list) -> float:
    x = circle_coordinate[0] - center_coordinate[0]
    y = circle_coordinate[1] - center_coordinate[1]

    circle_radius = math.sqrt(x * x + y * y)

    return circle_radius


def get_triangle_area(coordinates: list) -> float:
    ab = math.sqrt((coordinates[1][0] - coordinates[0][0]) *
                   (coordinates[1][0] - coordinates[0][0]) +
                   (coordinates[1][1] - coordinates[0][1]) *
                   (coordinates[1][1] - coordinates[0][1]))
    bc = math.sqrt((coordinates[2][0] - coordinates[1][0]) *
                   (coordinates[2][0] - coordinates[1][0]) +
                   (coordinates[2][1] - coordinates[1][1]) *
                   (coordinates[2][1] - coordinates[1][1]))
    ca = math.sqrt((coordinates[0][0] - coordinates[2][0]) *
                   (coordinates[0][0] - coordinates[2][0]) +
                   (coordinates[0][1] - coordinates[2][1]) *
                   (coordinates[0][1] - coordinates[2][1]))

    half_perimeter = (ab + bc + ca) / 2

    triangle_area = math.sqrt(half_perimeter * (half_perimeter - ab) *
                              (half_perimeter - bc) * (half_perimeter - ca))

    return triangle_area


def get_rectangle_area(coordinates: list) -> float:
    triangle_area_1 = get_triangle_area(coordinates[:3])
    triangle_area_2 = get_triangle_area([coordinates[0],
                                         coordinates[2], coordinates[3]])

    rectangle_area = triangle_area_1 + triangle_area_2

    return rectangle_area


def get_tangent_coefficients(circle_center_2: list, radius_1: float,
                             radius_2: float) -> list:
    d_1 = radius_1
    d_2 = radius_2

    v_x = circle_center_2[0]
    v_y = circle_center_2[1]

    if abs(v_x * v_x + v_y * v_y) < 1e-3:
        return None

    a = ((d_2 - d_1) * v_x + v_y *
         math.sqrt(v_x * v_x + v_y * v_y -
                   ((d_2 - d_1) * (d_2 - d_1)))) / (v_x * v_x + v_y * v_y)
    b = ((d_2 - d_1) * v_y - v_x *
         math.sqrt(v_x * v_x + v_y * v_y -
                   ((d_2 - d_1) * (d_2 - d_1)))) / (v_x * v_x + v_y * v_y)
    c = d_1

    return [a, b, c]


def get_tangent_coordinates(circle_center_1: list, radius_1: float,
                            circle_center_2: list, radius_2: float) -> list:
    current_circle_center_1 = circle_center_1.copy()
    current_circle_center_2 = circle_center_2.copy()

    if abs(circle_center_1[0]) > EPS or abs(circle_center_1[1]) > EPS:
        new_x = circle_center_1[0]
        new_y = circle_center_1[1]

        current_circle_center_2[0] -= new_x
        current_circle_center_2[1] -= new_y

        current_circle_center_1[0] = 0
        current_circle_center_1[1] = 0

        try:
            a, b, c = get_tangent_coefficients(current_circle_center_1,
                                               current_circle_center_2,
                                               radius_1, radius_2)
        except TypeError:
            return [None]
    else:
        try:
            a, b, c = get_tangent_coefficients(circle_center_1, circle_center_2,
                                               radius_1, radius_2)
        except TypeError:
            return [None]

        new_x = 0
        new_y = 0

    matrix_1 = np.array([[b, -a], [a, b]])
    vector_1 = np.array(
        [-a * current_circle_center_1[1] + b * current_circle_center_1[0],
         -c])
    coordinates_1 = np.linalg.solve(matrix_1, vector_1)

    matrix_2 = np.array([[b, -a], [a, b]])
    vector_2 = np.array(
        [-a * current_circle_center_2[1] + b * current_circle_center_2[0],
         -c])
    coordinates_2 = np.linalg.solve(matrix_2, vector_2)

    coordinates_1 = coordinates_1.tolist()
    coordinates_2 = coordinates_2.tolist()

    result = list()

    result.append(coordinates_1[0] + new_x)
    result.append(coordinates_1[1] + new_y)

    result.append(coordinates_2[0] + new_x)
    result.append(coordinates_2[1] + new_y)

    return result


def get_min_x(coordinates: list) -> float:
    result = coordinates[0][0]

    for number in coordinates:
        if number[0] < result:
            result = number[0]

    return result


def get_max_x(coordinates: list) -> float:
    result = coordinates[0][0]

    for number in coordinates:
        if number[0] > result:
            result = number[0]

    return result


def get_min_y(coordinates: list) -> float:
    result = coordinates[0][1]

    for number in coordinates:
        if number[1] < result:
            result = number[1]

    return result


def get_max_y(coordinates: list) -> float:
    result = coordinates[0][1]

    for number in coordinates:
        if number[1] > result:
            result = number[1]

    return result


def get_critical_points(circle_center_1: list, radius_1: float,
                        circle_center_2: list, radius_2: float) -> list:
    coordinates = [[0, 0], [circle_center_1[0] - radius_1,
                            circle_center_1[1]],
                   [circle_center_1[0] + radius_1,
                    circle_center_1[1]],
                   [circle_center_1[0],
                    circle_center_1[1] - radius_1],
                   [circle_center_1[0],
                    circle_center_1[1] + radius_1],
                   [circle_center_2[0] - radius_2,
                    circle_center_2[1]],
                   [circle_center_2[0] + radius_2,
                    circle_center_2[1]],
                   [circle_center_2[0],
                    circle_center_2[1] - radius_2],
                   [circle_center_2[0],
                    circle_center_2[1] + radius_2]]

    x_min = get_min_x(coordinates)
    x_max = get_max_x(coordinates)

    y_min = get_min_y(coordinates)
    y_max = get_max_y(coordinates)

    return [x_min, x_max, y_min, y_max]


def get_scale_coefficient(canvas_size: list, critical_points: list) -> float:
    k_x = (canvas_size[2] - canvas_size[0]) / \
          (critical_points[1] - critical_points[0])
    k_y = (canvas_size[3] - canvas_size[1]) / \
          (critical_points[3] - critical_points[2])

    return min(k_x, k_y)


def draw_circle(x_c: float, y_c: float, radius: float, x_min: float,
                y_max: float, k: float, canvas_name, outline: str, width: int):
    x_0 = x_c - radius
    y_0 = y_c - radius

    x_1 = x_c + radius
    y_1 = y_c + radius

    x_0 = round(15 + (x_0 - x_min) * k)
    y_0 = round(15 + (y_max - y_0) * k)

    x_1 = round(15 + (x_1 - x_min) * k)
    y_1 = round(15 + (y_max - y_1) * k)

    canvas_name.create_oval(x_0, y_0, x_1, y_1, outline=outline, width=width)


def draw_segment(x_0: float, y_0: float, x_1: float, y_1: float, x_min: float,
                 y_max: float, k: float, canvas_name, fill: str, width: int):
    x_t_1 = x_0
    y_t_1 = y_0

    x_t_2 = x_1
    y_t_2 = y_1

    x_0 = round(15 + (x_0 - x_min) * k)
    y_0 = round(15 + (y_max - y_0) * k)

    x_1 = round(15 + (x_1 - x_min) * k)
    y_1 = round(15 + (y_max - y_1) * k)

    canvas_name.create_line(x_0, y_0, x_1, y_1,
                            fill=fill, width=width)

    canvas_name.create_text(x_0, y_0 + 20,
                            text='({:.2f}; {:.2f})'.format(x_t_1, y_t_1),
                            font=8)
    canvas_name.create_text(x_1, y_1 + 20,
                            text='({:.2f}; {:.2f})'.format(x_t_2, y_t_2),
                            font=8)


def draw_axes(canvas_size: list, x_min: float, y_max: float, k: float,
              canvas_name, fill: str, width: int):
    x_0 = 0
    x_1 = canvas_size[2]

    y_0 = 0
    y_1 = 0

    y_0 = round(15 + (y_max - y_0) * k)
    y_1 = round(15 + (y_max - y_1) * k)

    canvas_name.create_line(x_0, y_0, x_1, y_1,
                            fill=fill, width=width)

    x_0 = 0
    x_1 = 0

    y_0 = 0
    y_1 = canvas_size[3]

    x_0 = round(15 + (x_0 - x_min) * k)
    x_1 = round(15 + (x_1 - x_min) * k)

    canvas_name.create_line(x_0, y_0, x_1, y_1,
                            fill=fill, width=width)
