def vector_product(vector_0, vector_1):
    return vector_0[0] * vector_1[1] - vector_0[1] * vector_1[0]


def scalar_product(vector_0, vector_1):
    return vector_0[0] * vector_1[0] + vector_0[1] * vector_1[1]


def get_vector(dot_0, dot_1):
    return [dot_1[0] - dot_0[0], dot_1[1] - dot_0[1]]


def get_lines_parametric_intersection(line_0, line_1, normal):
    d = get_vector(line_0[0], line_0[1])
    w = get_vector(line_1[0], line_0[0])

    d_scalar = scalar_product(d, normal)
    w_scalar = scalar_product(w, normal)

    t = -w_scalar / d_scalar

    return [line_0[0][0] + d[0] * t, line_0[0][1] + d[1] * t]


def is_visible(dot, f_dot, s_dot):
    vector_0 = get_vector(f_dot, s_dot)
    vector_1 = get_vector(f_dot, dot)

    if vector_product(vector_0, vector_1) <= 0:
        return True
    else:
        return False


def get_normal(dot_0, dot_1, dot_2):
    vector = get_vector(dot_0, dot_1)

    if vector[1]:
        normal = [1, - vector[0] / vector[1]]
    else:
        normal = [0, 1]

    if scalar_product(get_vector(dot_1, dot_2), normal) < 0:
        normal[0] = -normal[0]
        normal[1] = -normal[1]

    return normal


def sutherland_hodgman_algorithm(clipper_line, trial_point, figure):
    current_result = []

    dot_0 = clipper_line[0]
    dot_1 = clipper_line[1]

    normal = get_normal(dot_0, dot_1, trial_point)
    prev_vision = is_visible(figure[-2], dot_0, dot_1)

    for i in range(-1, len(figure)):
        cur_vision = is_visible(figure[i], dot_0, dot_1)

        if prev_vision:
            if cur_vision:
                current_result.append(figure[i])
            else:
                figure_line = [figure[i - 1], figure[i]]
                current_result.append(get_lines_parametric_intersection(figure_line, clipper_line, normal))
        else:
            if cur_vision:
                figure_line = [figure[i - 1], figure[i]]
                current_result.append(get_lines_parametric_intersection(figure_line, clipper_line, normal))
                current_result.append(figure[i])

        prev_vision = cur_vision

    return current_result
