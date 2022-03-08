def parse_coordinate(string: str) -> list:
    flag = True

    try:
        result = list(map(float, string.split(', ')))
    except ValueError:
        flag = False

    if flag:
        return result

    flag = True

    try:
        result = list(map(float, string.split('; ')))
    except ValueError:
        flag = False

    if flag:
        return result

    flag = True

    try:
        result = list(map(float, string.split(' ')))
    except ValueError:
        flag = False

    if not flag:
        return [None]

    return result
