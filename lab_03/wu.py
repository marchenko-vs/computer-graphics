def test_wu(ps, pf):
    x1 = ps[0]
    x2 = pf[0]
    y1 = ps[1]
    y2 = pf[1]
    I = 100
    stairs = []

    if x1 == x2 and y1 == y2:
        flag = 1

    steep = abs(y2 - y1) > abs(x2 - x1)

    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        tg = 1
    else:
        tg = dy / dx

    xend = round(x1)
    yend = y1 + tg * (xend - x1)
    xpx1 = xend
    ypx1 = int(yend)
    y = yend + tg

    xend = int(x2 + 0.5)
    yend = y2 + tg * (xend - x2)
    xpx2 = xend

    if steep:
        for x in range(xpx1, xpx2):

            y += tg
    else:
        for x in range(xpx1, xpx2):
            y += tg
