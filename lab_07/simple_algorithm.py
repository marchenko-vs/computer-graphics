import numpy as np


def get_bin_codes(line, left_side, right_side, bottom_side, top_side):
    code_begin_point = 0b0000
    code_end_point = 0b0000

    if line[0][0] < left_side:
        code_begin_point += 0b1000

    if line[0][0] > right_side:
        code_begin_point += 0b0100

    if line[0][1] > bottom_side:
        code_begin_point += 0b0010

    if line[0][1] < top_side:
        code_begin_point += 0b0001

    if line[1][0] < left_side:
        code_end_point += 0b1000

    if line[1][0] > right_side:
        code_end_point += 0b0100

    if line[1][1] > bottom_side:
        code_end_point += 0b0010

    if line[1][1] < top_side:
        code_end_point += 0b0001

    return code_begin_point, code_end_point


def simple_algorithm(lines, line, left_side, right_side, bottom_side, top_side):
    bin_codes = get_bin_codes(lines[line], left_side, right_side, bottom_side, top_side)

    code_begin_point = bin_codes[0]
    code_end_point = bin_codes[1]

    if code_begin_point == 0 and code_end_point == 0:
        return lines[line]

    if code_begin_point & code_end_point:
        return []

    begin_coordinates = lines[line][0]
    end_coordinates = lines[line][1]

    flag = 1
    i = -1
    tangent = 1e30

    if not code_begin_point:
        result = [begin_coordinates]
        workVar = end_coordinates
        i = 1
        flag = 0
    elif not code_end_point:
        result = [end_coordinates]
        workVar = begin_coordinates
        i = 1
        flag = 0
    else:
        result = []

    while i <= 1:
        if flag:
            workVar = lines[line][i]

        i += 1

        if begin_coordinates[0] != end_coordinates[0]:
            tangent = (end_coordinates[1] - begin_coordinates[1]) / (end_coordinates[0] - begin_coordinates[0])

            if workVar[0] <= left_side:
                crosser = tangent * (left_side - workVar[0]) + workVar[1]

                if (crosser <= bottom_side) and (crosser >= top_side):
                    result.append([left_side, int(np.round(crosser))])
                    continue
            elif workVar[0] >= right_side:
                crosser = tangent * (right_side - workVar[0]) + workVar[1]

                if (crosser <= bottom_side) and (crosser >= top_side):
                    result.append([right_side, int(np.round(crosser))])
                    continue

        if begin_coordinates[1] != end_coordinates[1]:
            if workVar[1] <= top_side:
                crosser = (top_side - workVar[1]) / tangent + workVar[0]

                if (crosser >= left_side) and (crosser <= right_side):
                    result.append([int(np.round(crosser)), top_side])
                    continue
            elif workVar[1] >= bottom_side:
                crosser = (bottom_side - workVar[1]) / tangent + workVar[0]

                if (crosser >= left_side) and (crosser <= right_side):
                    result.append([int(np.round(crosser)), bottom_side])
                    continue

    return result
