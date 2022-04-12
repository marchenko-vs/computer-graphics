from graphics_math import sign, get_rgb_intensity


# Брезенхема со сглаживанием
def smoth_test(ps, pf):
    L = 100
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        pr = 1
    else:
        pr = 0
    m = dy / dx * L
    e = L / 2
    w = L - m
    x = ps[0]
    y = ps[1]
    while x != pf[0] or y != pf[1]:
        if e < w:
            if pr == 0:
                x += sx
            else:
                y += sy
            e += m
        elif e >= w:
            x += sx
            y += sy
            e -= w


def draw_line_brez_smoth(canvas, ps, pf, fill):
    I = 100
    fill = get_rgb_intensity(canvas, fill, I)
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        steep = 1 #
    else:
        steep = 0 #
    tg = dy / dx * I # тангенс угла наклона (умножаем на инт., чтобы не приходилось умножать внутри цикла
    e = I / 2 # интенсивность для высвечивания начального пикселя
    w = I - tg # пороговое значение
    x = ps[0]
    y = ps[1]
    stairs = []
    st = 1
    while x != pf[0] or y != pf[1]:
        canvas.create_line(x, y, x + 1, y + 1, fill=fill[round(e) - 1])
        if e < w:
            if steep == 0: # dy < dx
                x += sx # -1 if dx < 0, 0 if dx = 0, 1 if dx > 0
            else: # dy >= dx
                y += sy # -1 if dy < 0, 0 if dy = 0, 1 if dy > 0
            st += 1 # stepping
            e += tg
        elif e >= w:
            x += sx
            y += sy
            e -= w
            stairs.append(st)
            st = 0
    if st:
        stairs.append(st)
    return stairs


# БР вещественный для теста
def float_test(ps, pf):
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        pr = 1
    else:
        pr = 0
    m = dy / dx
    e = m - 1 / 2
    x = ps[0]
    y = ps[1]
    while x != pf[0] or y != pf[1]:
        if e >= 0:
            if pr == 1:
                x += sx
            else:
                y += sy
            e -= 1
        if e <= 0:
            if pr == 0:
                x += sx
            else:
                y += sy
        e += m


# Брезенхема с действительными коэффами
def draw_line_brez_float(canvas, ps, pf, fill):
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    
    if dy >= dx:
        dx, dy = dy, dx
        steep = 1 # шагаем по y
    else:
        steep = 0
        
    tg = dy / dx # tангенс угла наклона
    e = tg - 1 / 2 # начальное значение ошибки
    x = ps[0] # начальный икс
    y = ps[1] # начальный игрек
    stairs = []
    st = 1
    while x != pf[0] or y != pf[1]:
        canvas.create_line(x, y, x + 1, y + 1, fill=fill)
        # выбираем пиксель
        if e >= 0:
            if steep == 1: # dy >= dx
                x += sx
            else: # dy < dx
                y += sy
            e -= 1 # отличие от целого
            stairs.append(st)
            st = 0
        if e <= 0:
            if steep == 0: # dy < dx
                x += sx
            else: # dy >= dx
                y += sy
            st += 1
            e += tg # отличие от целого

    if st:
        stairs.append(st)
    return stairs


# БР целый
def int_test(ps, pf):
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        pr = 1
    else:
        pr = 0
    m = 2 * dy
    e = m - dx
    ed = 2 * dx
    x = ps[0]
    y = ps[1]
    while x != pf[0] or y != pf[1]:
        if e >= 0:
            if pr == 1:
                x += sx
            else:
                y += sy
            e -= ed
        if e <= 0:
            if pr == 0:
                x += sx
            else:
                y += sy
        e += m


# Брезенхема с целыми коэффами
def draw_line_brez_int(canvas, ps, pf, fill):
    dx = pf[0] - ps[0]
    dy = pf[1] - ps[1]
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        steep = 1
    else:
        steep = 0
    e = 2 * dy - dx # отличие от вещественного (e = tg - 1 / 2) tg = dy / dx
    x = ps[0]
    y = ps[1]
    stairs = []
    st = 1
    while x != pf[0] or y != pf[1]:
        canvas.create_line(x, y, x + 1, y + 1, fill=fill)
        if e >= 0:
            if steep == 1:
                x += sx
            else:
                y += sy
            stairs.append(st)
            st = 0
            e -= 2 * dx # отличие от вещественного (e -= 1)
        if e <= 0:
            if steep == 0:
                x += sx
            else:
                y += sy
            st += 1
            e += 2 * dy # difference (e += tg)

    if st:
        stairs.append(st)
    return stairs

