EPS = 1e-3


def get_dot_product(vector_1, vector_2):
    return vector_1[0] * vector_2[0] + vector_1[1] * vector_2[1]


def get_vector(dot_1, dot_2):
    return [dot_2[0] - dot_1[0], dot_2[1] - dot_1[1]]


def get_normal(dot_1, dot_2, dot_3):
    vector_1 = get_vector(dot_1, dot_2)

    if abs(vector_1[1]) > EPS:
        normal = [1, -(vector_1[0] / vector_1[1])]
    else:
        normal = [0, 1]

    vector_2 = get_vector(dot_2, dot_3)

    if get_dot_product(vector_2, normal) < 0:
        normal[0] = -normal[0]
        normal[1] = -normal[1]

    return normal


def cyrus_beck_algorithm(line, clipping_window, color, canvas):
    dot_1 = line[0]
    dot_2 = line[1]

    d = [dot_2[0] - dot_1[0], dot_2[1] - dot_1[1]]

    t_min = 0
    t_max = 1

    for i in range(-2, len(clipping_window) - 2):
        normal = get_normal(clipping_window[i], clipping_window[i + 1], clipping_window[i + 2])

        w = [dot_1[0] - clipping_window[i][0],
             dot_1[1] - clipping_window[i][1]]

        d_scalar = get_dot_product(d, normal)
        w_scalar = get_dot_product(w, normal)

        if d_scalar == 0:
            if w_scalar < 0:
                return
            else:
                continue

        t = -(w_scalar / d_scalar)

        if d_scalar > 0:
            if t <= 1:
                t_min = max(t_min, t)
            else:
                return
        elif d_scalar < 0:
            if t >= 0:
                t_max = min(t_max, t)
            else:
                return

        if t_min > t_max:
            break

    if t_min <= t_max:
        dot1_res = [round(dot_1[0] + d[0] * t_min), round(dot_1[1] + d[1] * t_min)]
        dot2_res = [round(dot_1[0] + d[0] * t_max), round(dot_1[1] + d[1] * t_max)]

        canvas.create_line(dot1_res, dot2_res, fill=color)
