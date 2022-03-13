import tkinter as tk
import graphics_math as gm


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 550

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
main_canvas.pack(side='top')

center_label = tk.Label(text='Центр масштабирования/поворота', font=15)
center_label.place(x=80, y=580)

center_label_x = tk.Label(text='Xc', font=15)
center_label_x.place(x=110, y=625)

center_label_y = tk.Label(text='Yc', font=15)
center_label_y.place(x=110, y=665)

center_entry_x = tk.Entry(font='Calibri 15', width=10, justify='center')
center_entry_x.place(x=150, y=620)

center_entry_y = tk.Entry(font='Calibri 15', width=10, justify='center')
center_entry_y.place(x=150, y=660)

transfer_label = tk.Label(text='Перенос', font=15)
transfer_label.place(x=480, y=580)

transfer_label_x = tk.Label(text='dX', font=15)
transfer_label_x.place(x=410, y=625)

transfer_label_y = tk.Label(text='dY', font=15)
transfer_label_y.place(x=410, y=665)

transfer_entry_x = tk.Entry(font='Calibri 15', width=10, justify='center')
transfer_entry_x.place(x=450, y=620)

transfer_entry_y = tk.Entry(font='Calibri 15', width=10, justify='center')
transfer_entry_y.place(x=450, y=660)

scale_label = tk.Label(text='Масштабирование', font=15)
scale_label.place(x=740, y=580)

scale_label_x = tk.Label(text='Kx', font=15)
scale_label_x.place(x=710, y=625)

scale_label_y = tk.Label(text='Ky', font=15)
scale_label_y.place(x=710, y=665)

scale_entry_x = tk.Entry(font='Calibri 15', width=10, justify='center')
scale_entry_x.place(x=750, y=620)

scale_entry_y = tk.Entry(font='Calibri 15', width=10, justify='center')
scale_entry_y.place(x=750, y=660)

rotate_label = tk.Label(text='Поворот', font=15)
rotate_label.place(x=1080, y=580)

rotate_entry_x = tk.Entry(font='Calibri 15', width=10, justify='center')
rotate_entry_x.place(x=1050, y=620)

rotate_label_phi = tk.Label(text='α', font=20)
rotate_label_phi.place(x=1025, y=625)

submit_button = tk.Button(text='Получить решение', font=15)
submit_button.place(x=950, y=660)

cancel_button = tk.Button(text='Отмена', font=15)
cancel_button.place(x=1150, y=660)

main_window.mainloop()

