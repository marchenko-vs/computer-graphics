def draw_circle(canvas_size: list, x_c: float, y_c: float, radius: float,
                k_x: float, k_y: float, canvas_name, outline: str, width: int):
    x_0 = x_c - radius
    y_0 = y_c - radius

    x_1 = x_c + radius
    y_1 = y_c + radius

    x_0 = round(canvas_size[2] / 2 + (x_0 * k_x))
    y_0 = round(canvas_size[3] / 2 + (y_0 * k_y))

    x_1 = round(canvas_size[2] / 2 + (x_1 * k_x))
    y_1 = round(canvas_size[3] / 2 + (y_1 * k_y))

    canvas_name.create_oval(x_0, y_0, x_1, y_1, outline=outline, width=width)

    return

