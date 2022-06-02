def get_bin_codes(line, left_side, right_side, bottom_side, top_side):
    firstPoint = 0b0000
    secondPoint = 0b0000

    if line[0][0] < left_side:
        firstPoint += 0b1000

    if line[0][0] > right_side:
        firstPoint += 0b0100

    if line[0][1] > bottom_side:
        firstPoint += 0b0010

    if line[0][1] < top_side:
        firstPoint += 0b0001

    if line[1][0] < left_side:
        secondPoint += 0b1000

    if line[1][0] > right_side:
        secondPoint += 0b0100

    if line[1][1] > bottom_side:
        secondPoint += 0b0010

    if line[1][1] < top_side:
        secondPoint += 0b0001

    return firstPoint, secondPoint


def simple_algorithm(lines, line, left_side, right_side, bottom_side, top_side):
    binCodes = get_bin_codes(lines[line], left_side, right_side, bottom_side, top_side)

    firstPoint = binCodes[0]
    secondPoint = binCodes[1]
    fCoordinates = lines[line][0]
    sCoordinates = lines[line][1]

    if firstPoint == 0 and secondPoint == 0:
        return lines[line]

    if firstPoint & secondPoint:
        return []

    flag = 1
    i = -1
    tan = 1e30

    if not firstPoint:
        result = [fCoordinates]
        workVar = sCoordinates
        i = 1
        flag = 0
    elif not secondPoint:
        result = [sCoordinates]
        workVar = fCoordinates
        i = 1
        flag = 0
    else:
        result = []

    while i <= 1:
        if flag:
            workVar = lines[line][i]

        i += 1

        if fCoordinates[0] != sCoordinates[0]:
            tan = (sCoordinates[1] - fCoordinates[1]) / (sCoordinates[0] - fCoordinates[0])

            if workVar[0] <= left_side:
                crosser = tan * (left_side - workVar[0]) + workVar[1]

                if (crosser <= bottom_side) and (crosser >= top_side):
                    result.append([left_side, int(round(crosser))])
                    continue
            elif workVar[0] >= right_side:
                crosser = tan * (right_side - workVar[0]) + workVar[1]

                if (crosser <= bottom_side) and (crosser >= top_side):
                    result.append([right_side, int(round(crosser))])
                    continue

        if fCoordinates[1] != sCoordinates[1]:
            if workVar[1] <= top_side:
                crosser = (top_side - workVar[1]) / tan + workVar[0]

                if (crosser >= left_side) and (crosser <= right_side):
                    result.append([int(round(crosser)), top_side])
                    continue
            elif workVar[1] >= bottom_side:
                crosser = (bottom_side - workVar[1]) / tan + workVar[0]

                if (crosser >= left_side) and (crosser <= right_side):
                    result.append([int(round(crosser)), bottom_side])
                    continue

    return result
