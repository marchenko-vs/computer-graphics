from graphics_math import sign


def test_bresenham_smooth(ps, pf):
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
