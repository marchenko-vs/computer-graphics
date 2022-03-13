import tkinter as tk
import graphics_math as gm


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 700

CURRENT_X_C = 0
CURRENT_Y_C = 0
CURRENT_RADIUS = 5

SCALE_X = 1
SCALE_Y = 1

TRANSFER_X = 0
TRANSFER_Y = 0


def scale_object():
    k_x = scale_entry_x.get()
    k_y = scale_entry_y.get()

    flag_x = False
    flag_y = False

    if k_x == '':
        k_x = 1
        flag_x = True

    if k_y == '':
        k_y = 1
        flag_y = True

    if not flag_x:
        try:
            k_x = float(k_x)
        except ValueError:
            print('False')

    if not flag_y:
        try:
            k_y = float(k_y)
        except ValueError:
            print('False')

    global SCALE_X
    global SCALE_Y

    SCALE_X *= k_x
    SCALE_Y *= k_y

    main_canvas.delete('all')

    gm.draw_circle([0, 0, CANVAS_WIDTH, CANVAS_HEIGHT], 0, 0, 5, SCALE_X,
                   SCALE_Y, main_canvas, 'black', 2)


def transfer_object():
    d_x = transfer_entry_x.get()
    d_y = transfer_entry_y.get()

    flag_x = False
    flag_y = False

    if d_x == '':
        d_x = 1
        flag_x = True

    if d_y == '':
        d_y = 1
        flag_y = True

    if not flag_x:
        try:
            d_x = float(d_x)
        except ValueError:
            print('False')

    if not flag_y:
        try:
            d_y = float(d_y)
        except ValueError:
            print('False')

    global TRANSFER_X
    global TRANSFER_Y

    TRANSFER_X += d_x
    TRANSFER_Y += d_y

    main_canvas.delete('all')

    gm.draw_circle([0, 0, CANVAS_WIDTH, CANVAS_HEIGHT], 0 + TRANSFER_X,
                   0 + TRANSFER_Y, 5, 1, 1, main_canvas, 'black', 2)


main_window = tk.Tk()
main_window.title('Лабораторная работа #2')
main_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+150+150')
main_window.resizable(width=False, height=False)

main_canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                        background='white')
main_canvas.pack(side='right')

center_entry_x = tk.Entry()
center_entry_x.place(x=20, y=20)

center_entry_y = tk.Entry()
center_entry_y.place(x=20, y=50)

scale_entry_x = tk.Entry()
scale_entry_x.place(x=20, y=100)

scale_entry_y = tk.Entry()
scale_entry_y.place(x=20, y=130)

scale_button = tk.Button(text='Масштабировать', command=scale_object)
scale_button.place(x=20, y=160)

transfer_entry_x = tk.Entry()
transfer_entry_x.place(x=20, y=190)

transfer_entry_y = tk.Entry()
transfer_entry_y.place(x=20, y=220)

transfer_button = tk.Button(text='Перенести', command=transfer_object)
transfer_button.place(x=20, y=250)

main_window.mainloop()
