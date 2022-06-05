def get_vector(dot1, dot2):
    return [dot2[0] - dot1[0], dot2[1] - dot1[1]]


def vector_mul(vec1, vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


def scalar_mul(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


def get_normal(dot1, dot2, dot3):
    vector = get_vector(dot1, dot2)

    if vector[1]:
        normal = [1, - vector[0] / vector[1]]
    else:
        normal = [0, 1]

    if scalar_mul(get_vector(dot2, dot3), normal) < 0:
        normal[0] = - normal[0]
        normal[1] = - normal[1]

    return normal


def is_visible(dot, f_dot, s_dot):
    vec1 = get_vector(f_dot, s_dot)
    vec2 = get_vector(f_dot, dot)

    if vector_mul(vec1, vec2) <= 0:
        return True
    else:
        return False


def get_lines_parametric_intersection(line1, line2, normal):
    d = get_vector(line1[0], line1[1])
    w = get_vector(line2[0], line1[0])

    d_scalar = scalar_mul(d, normal)
    w_scalar = scalar_mul(w, normal)

    t = -w_scalar / d_scalar

    return [line1[0][0] + d[0] * t, line1[0][1] + d[1] * t]


def sutherland_hodgman_algorithm(clipper_line, position, figure):
    current_result = []

    dot1 = clipper_line[0]
    dot2 = clipper_line[1]

    normal = get_normal(dot1, dot2, position)
    prev_vision = is_visible(figure[-2], dot1, dot2)

    for i in range(-1, len(figure)):
        cur_vision = is_visible(figure[i], dot1, dot2)

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
