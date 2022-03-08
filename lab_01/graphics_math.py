import math
import numpy as np


EPS = 1e-3


def draw_axes(canvas_name, canvas_width: int, canvas_height: int):
    canvas_name.create_line(canvas_width / 2, 0,
                            canvas_width / 2, canvas_height)
    canvas_name.create_line(0, canvas_height / 2,
                            canvas_width, canvas_height / 2)


def get_circle_center(coordinates: list) -> list:
    x_12 = coordinates[0][0] - coordinates[1][0]
    x_23 = coordinates[1][0] - coordinates[2][0]
    x_31 = coordinates[2][0] - coordinates[0][0]

    y_12 = coordinates[0][1] - coordinates[1][1]
    y_23 = coordinates[1][1] - coordinates[2][1]
    y_31 = coordinates[2][1] - coordinates[0][1]

    z_1 = coordinates[0][0] * coordinates[0][0] + coordinates[0][1] * \
          coordinates[0][1]
    z_2 = coordinates[1][0] * coordinates[1][0] + coordinates[1][1] * \
          coordinates[1][1]
    z_3 = coordinates[2][0] * coordinates[2][0] + coordinates[2][1] * \
          coordinates[2][1]

    try:
        a = - ((y_12 * z_3 + y_23 * z_1 + y_31 * z_2) /
               (2 * (x_12 * y_31 - y_12 * x_31)))
        b = (x_12 * z_3 + x_23 * z_1 + x_31 * z_2) / \
            (2 * (x_12 * y_31 - y_12 * x_31))
    except ZeroDivisionError:
        return [None, None]

    return [a, b]


def get_triangle_area(ab: float, bc: float, ca: float) -> float:
    half_perimeter = (ab + bc + ca) / 2

    triangle_area = math.sqrt(half_perimeter * (half_perimeter - ab) *
                              (half_perimeter - bc) * (half_perimeter - ca))

    return triangle_area


def get_circle_radius(coordinates: list) -> float:
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

    triangle_area = get_triangle_area(ab, bc, ca)
    circle_radius = ab * bc * ca / (4 * triangle_area)

    return circle_radius


def get_rectangle_area(coordinates: list) -> float:
    ab = math.sqrt((coordinates[1][0] - coordinates[0][0]) *
                   (coordinates[1][0] - coordinates[0][0]) +
                   (coordinates[1][1] - coordinates[0][1]) *
                   (coordinates[1][1] - coordinates[0][1]))
    bc = math.sqrt((coordinates[2][0] - coordinates[1][0]) *
                   (coordinates[2][0] - coordinates[1][0]) +
                   (coordinates[2][1] - coordinates[1][1]) *
                   (coordinates[2][1] - coordinates[1][1]))
    cd = math.sqrt((coordinates[3][0] - coordinates[2][0]) *
                   (coordinates[3][0] - coordinates[2][0]) +
                   (coordinates[3][1] - coordinates[2][1]) *
                   (coordinates[3][1] - coordinates[2][1]))
    da = math.sqrt((coordinates[0][0] - coordinates[3][0]) *
                   (coordinates[0][0] - coordinates[3][0]) +
                   (coordinates[0][1] - coordinates[3][1]) *
                   (coordinates[0][1] - coordinates[3][1]))

    half_perimeter = (ab + bc + cd + da) / 2

    rectangle_area = math.sqrt((half_perimeter - ab) * (half_perimeter - bc) *
                               (half_perimeter - cd) * (half_perimeter - da))

    return rectangle_area


def draw_circle(x: float, y: float, radius: float, canvas_name, color: str):
    x_0 = x - radius
    y_0 = y - radius
    x_1 = x + radius
    y_1 = y + radius

    if radius > 225:
        k = 225 / radius
        x_0 *= k
        y_0 *= k
        x_1 *= k
        y_1 *= k

    canvas_name.create_oval(x_0 + 275, -y_0 + 225, x_1 + 275, -y_1 + 225,
                            outline=color)


def line_function(x: float, a: float, b: float, c: float) -> float:
    return - (c + a * x) / b


def draw_line(min_limit: float, max_limit: float, a: float, b: float,
              c: float, canvas_name, color: str):
    while min_limit < max_limit:
        x = min_limit
        y = line_function(x, a, b, c)
        canvas_name.create_oval(x + 275, -y + 225, x + 275, -y + 225,
                                outline=color)
        min_limit += 0.01


def draw_segment(x_0: float, y_0: float, x_1: float, y_1: float, canvas_name,
                 color: str):
    canvas_name.create_line(x_0 + 275, -y_0 + 225, x_1 + 275, -y_1 + 225,
                            fill=color)


def get_tangent_coefficients(circle_center_1: list, circle_center_2: list,
                             radius_1: float, radius_2: float) -> list:
    d_1 = radius_1
    d_2 = radius_2

    v_x = circle_center_2[0]
    v_y = circle_center_2[1]

    if abs(v_x * v_x + v_y * v_y) < 1e-3:
        return None

    a = ((d_2 - d_1) * v_x + v_y *
         math.sqrt(v_x * v_x + v_y * v_y +
                   ((d_2 - d_1) * (d_2 - d_1)))) / (v_x * v_x + v_y * v_y)
    b = ((d_2 - d_1) * v_y - v_x *
         math.sqrt(v_x * v_x + v_y * v_y -
                   ((d_2 - d_1) * (d_2 - d_1)))) / (v_x * v_x + v_y * v_y)
    c = d_1
    c -= a * circle_center_1[0] + b * circle_center_1[1]

    return [a, b, c]


def get_tangent_coordinates(circle_center_1: list, radius_1: float,
                            circle_center_2: list, radius_2: float) -> list:
    if abs(circle_center_1[0]) > EPS or abs(circle_center_1[1]) > EPS:
        new_x = circle_center_1[0]
        new_y = circle_center_1[1]

        circle_center_2[0] -= circle_center_1[0]
        circle_center_2[1] -= circle_center_1[1]

        circle_center_1[0] = 0
        circle_center_1[1] = 0

        try:
            a, b, c = get_tangent_coefficients(circle_center_1,
                                               circle_center_2, radius_1, radius_2)
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
    vector_1 = np.array([-a * circle_center_1[1] + b * circle_center_1[0],
                         -c])
    coordinates_1 = np.linalg.solve(matrix_1, vector_1)

    matrix_2 = np.array([[b, -a], [a, b]])
    vector_2 = np.array([-a * circle_center_2[1] + b * circle_center_2[0],
                         -c])
    coordinates_2 = np.linalg.solve(matrix_2, vector_2)

    coordinates_1 = coordinates_1.tolist()
    coordinates_2 = coordinates_2.tolist()

    result = list()

    result.append(int(coordinates_1[0]) + new_x)
    result.append(int(coordinates_1[1]) + new_y)

    result.append(int(coordinates_2[0]) + new_x)
    result.append(int(coordinates_2[1]) + new_y)

    circle_center_1[0] += new_x
    circle_center_1[1] += new_y

    circle_center_2[0] += new_x
    circle_center_2[1] += new_y

    return result
