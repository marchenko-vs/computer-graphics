import tkinter as tk
import graphics_math as gm
import objects as obj

from constants import *

building = obj.Rectangle([[-100, -80], [-100, 80], [100, 80], [100, -80]])
roof = obj.Triangle([[-100, 80], [0, 130], [100, 80]])
roof_window = obj.Rectangle([[-15, 90], [-15, 110], [15, 110], [15, 90]])
roof_window_lattice = obj.Lattice([[-15, 100], [0, 110], [15, 100], [0, 90]])
left_window = obj.Oval([[-85, 35], [-55, 65]])
left_window_lattice = obj.Lattice([[-85, 50], [-70, 35], [-55, 50], [-70, 65]])
door = obj.Oval([[30, -50], [70, 40]])
door_rectangle = obj.Rectangle([[30, -5], [50, 40], [70, -5], [50, -50]])
door_lattice = obj.Lattice([[30, -5], [50, -50], [70, -5], [50, 40]])
center_point = obj.CenterPoint(building.get_left_down(),
                               building.get_right_up(),
                               roof.get_up())


def _draw_house():
    gm.canvas_clear(main_canvas)

    left_window.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'brown', main_canvas)
    door.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'purple', main_canvas)

    gm.draw_axes([CANVAS_WIDTH, CANVAS_HEIGHT], 'lightgrey', main_canvas)

    building.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'green', main_canvas)
    roof.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'blue', main_canvas)
    roof_window.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'red', main_canvas)
    roof_window_lattice.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'red', main_canvas)
    left_window_lattice.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'brown',
                             main_canvas)
    door_rectangle.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'purple', main_canvas)
    door_lattice.draw([CANVAS_WIDTH, CANVAS_HEIGHT], 'purple', main_canvas)

    center_point.print([CANVAS_WIDTH, CANVAS_HEIGHT], main_canvas)


def _draw_init_house():
    global building
    global roof
    global roof_window
    global roof_window_lattice
    global left_window
    global left_window_lattice
    global door
    global door_rectangle
    global door_lattice
    global center_point

    building = obj.Rectangle([[-100, -80], [-100, 80], [100, 80], [100, -80]])
    roof = obj.Triangle([[-100, 80], [0, 130], [100, 80]])
    roof_window = obj.Rectangle([[-15, 90], [-15, 110], [15, 110], [15, 90]])
    roof_window_lattice = obj.Lattice(
        [[-15, 100], [0, 110], [15, 100], [0, 90]])
    left_window = obj.Oval([[-85, 35], [-55, 65]])
    left_window_lattice = obj.Lattice(
        [[-85, 50], [-70, 35], [-55, 50], [-70, 65]])
    door = obj.Oval([[30, -50], [70, 40]])
    door_rectangle = obj.Rectangle([[30, -5], [50, 40], [70, -5], [50, -50]])
    door_lattice = obj.Lattice([[30, -5], [50, -50], [70, -5], [50, 40]])
    center_point = obj.CenterPoint(building.get_left_down(),
                                   building.get_right_up(),
                                   roof.get_up())

    _draw_house()


def _transfer(cancel=False):
    roof.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                  transfer_entry_x, transfer_entry_y, main_canvas)
    roof_window.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                         transfer_entry_x, transfer_entry_y, main_canvas)
    roof_window_lattice.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                                 transfer_entry_x, transfer_entry_y,
                                 main_canvas)
    left_window.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                         transfer_entry_x, transfer_entry_y, main_canvas)
    left_window_lattice.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                                 transfer_entry_x, transfer_entry_y,
                                 main_canvas)
    door.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                  transfer_entry_x, transfer_entry_y, main_canvas)
    door_rectangle.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                            transfer_entry_x, transfer_entry_y, main_canvas)
    door_lattice.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                          transfer_entry_x, transfer_entry_y, main_canvas)
    building.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                      transfer_entry_x, transfer_entry_y, main_canvas)
    center_point.transfer([CANVAS_WIDTH, CANVAS_HEIGHT],
                          transfer_entry_x, transfer_entry_y, main_canvas)

    _draw_house()

    if not cancel:
        STEPS_LIST.append([TRANSFER, -float(transfer_entry_x.get()),
                           -float(transfer_entry_y.get())])


def _scale(cancel=False):
    roof.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
               scale_entry_x, scale_entry_y,
               center_entry_x, center_entry_y,
               main_canvas)
    roof_window.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                      scale_entry_x, scale_entry_y,
                      center_entry_x, center_entry_y,
                      main_canvas)
    roof_window_lattice.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                              scale_entry_x, scale_entry_y,
                              center_entry_x, center_entry_y,
                              main_canvas)
    left_window.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                      scale_entry_x, scale_entry_y,
                      center_entry_x, center_entry_y,
                      main_canvas)
    left_window_lattice.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                              scale_entry_x, scale_entry_y,
                              center_entry_x, center_entry_y,
                              main_canvas)
    door.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
               scale_entry_x, scale_entry_y,
               center_entry_x, center_entry_y,
               main_canvas)
    door_rectangle.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                         scale_entry_x, scale_entry_y,
                         center_entry_x, center_entry_y,
                         main_canvas)
    door_lattice.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                       scale_entry_x, scale_entry_y,
                       center_entry_x, center_entry_y,
                       main_canvas)
    building.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                   scale_entry_x, scale_entry_y,
                   center_entry_x, center_entry_y,
                   main_canvas)
    center_point.scale([CANVAS_WIDTH, CANVAS_HEIGHT],
                       scale_entry_x, scale_entry_y,
                       center_entry_x, center_entry_y,
                       main_canvas)

    _draw_house()

    if not cancel:
        scale_x = float(scale_entry_x.get())
        scale_y = float(scale_entry_y.get())

        if abs(scale_x) <= EPS or abs(scale_y) <= EPS:
            STEPS_LIST.append([INIT])
        else:
            STEPS_LIST.append([SCALE, 1 / scale_x,
                               1 / scale_y,
                               float(center_entry_x.get()),
                               float(center_entry_y.get())])


def _rotate(cancel=False):
    roof.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                rotate_entry,
                center_entry_x, center_entry_y,
                main_canvas)
    roof_window.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                       rotate_entry,
                       center_entry_x, center_entry_y,
                       main_canvas)
    roof_window_lattice.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                               rotate_entry,
                               center_entry_x, center_entry_y,
                               main_canvas)
    left_window_lattice.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                               rotate_entry,
                               center_entry_x, center_entry_y,
                               main_canvas)
    left_window.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                       rotate_entry,
                       center_entry_x, center_entry_y,
                       main_canvas)
    door.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                rotate_entry,
                center_entry_x, center_entry_y,
                main_canvas)
    door_rectangle.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                          rotate_entry,
                          center_entry_x, center_entry_y,
                          main_canvas)
    door_lattice.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                        rotate_entry,
                        center_entry_x, center_entry_y,
                        main_canvas)
    building.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                    rotate_entry,
                    center_entry_x, center_entry_y,
                    main_canvas)
    center_point.rotate([CANVAS_WIDTH, CANVAS_HEIGHT],
                        rotate_entry,
                        center_entry_x, center_entry_y,
                        main_canvas)

    _draw_house()

    if not cancel:
        STEPS_LIST.append([ROTATE, -float(rotate_entry.get()),
                           float(center_entry_x.get()),
                           float(center_entry_y.get())])


def _entries_init(event):
    tmp = center_entry_x.get()
    try:
        tmp = float(tmp)
    except ValueError:
        center_entry_x.delete(0, 'end')
        center_entry_x.insert(0, '0.0')

    tmp = center_entry_y.get()
    try:
        tmp = float(tmp)
    except ValueError:
        center_entry_y.delete(0, 'end')
        center_entry_y.insert(0, '0.0')

    tmp = transfer_entry_x.get()
    try:
        tmp = float(tmp)
    except ValueError:
        transfer_entry_x.delete(0, 'end')
        transfer_entry_x.insert(0, '0.0')

    tmp = transfer_entry_y.get()
    try:
        tmp = float(tmp)
    except ValueError:
        transfer_entry_y.delete(0, 'end')
        transfer_entry_y.insert(0, '0.0')

    tmp = scale_entry_x.get()
    try:
        tmp = float(tmp)
    except ValueError:
        scale_entry_x.delete(0, 'end')
        scale_entry_x.insert(0, '1.0')

    tmp = scale_entry_y.get()
    try:
        tmp = float(tmp)
    except ValueError:
        scale_entry_y.delete(0, 'end')
        scale_entry_y.insert(0, '1.0')

    tmp = rotate_entry.get()
    try:
        tmp = float(tmp)
    except ValueError:
        rotate_entry.delete(0, 'end')
        rotate_entry.insert(0, '0.0')


def _cancel():
    if STEPS_LIST == []:
        return

    step = STEPS_LIST.pop()

    if (step[0] == TRANSFER):
        x_tmp = transfer_entry_x.get()
        y_tmp = transfer_entry_y.get()

        transfer_entry_x.delete(0, 'end')
        transfer_entry_x.insert(0, str(step[1]))

        transfer_entry_y.delete(0, 'end')
        transfer_entry_y.insert(0, str(step[2]))

        _transfer(True)

        transfer_entry_x.delete(0, 'end')
        transfer_entry_x.insert(0, x_tmp)

        transfer_entry_y.delete(0, 'end')
        transfer_entry_y.insert(0, y_tmp)

    if (step[0] == SCALE):
        x_tmp = scale_entry_x.get()
        y_tmp = scale_entry_y.get()

        x_c_tmp = center_entry_x.get()
        y_c_tmp = center_entry_y.get()

        scale_entry_x.delete(0, 'end')
        scale_entry_x.insert(0, str(step[1]))

        scale_entry_y.delete(0, 'end')
        scale_entry_y.insert(0, str(step[2]))

        center_entry_x.delete(0, 'end')
        center_entry_x.insert(0, str(step[3]))

        center_entry_y.delete(0, 'end')
        center_entry_y.insert(0, str(step[4]))

        _scale(True)

        scale_entry_x.delete(0, 'end')
        scale_entry_x.insert(0, x_tmp)

        scale_entry_y.delete(0, 'end')
        scale_entry_y.insert(0, y_tmp)

        center_entry_x.delete(0, 'end')
        center_entry_x.insert(0, x_c_tmp)

        center_entry_y.delete(0, 'end')
        center_entry_y.insert(0, y_c_tmp)

    if (step[0] == ROTATE):
        x_tmp = rotate_entry.get()

        x_c_tmp = center_entry_x.get()
        y_c_tmp = center_entry_y.get()

        rotate_entry.delete(0, 'end')
        rotate_entry.insert(0, str(step[1]))

        center_entry_x.delete(0, 'end')
        center_entry_x.insert(0, str(step[2]))

        center_entry_y.delete(0, 'end')
        center_entry_y.insert(0, str(step[3]))

        _rotate(True)

        rotate_entry.delete(0, 'end')
        rotate_entry.insert(0, x_tmp)

        center_entry_x.delete(0, 'end')
        center_entry_x.insert(0, x_c_tmp)

        center_entry_y.delete(0, 'end')
        center_entry_y.insert(0, y_c_tmp)

    if step[0] == INIT:
        _draw_init_house()


def _cancel_all():
    for i in range(len(STEPS_LIST)):
        _cancel()


main_window = tk.Tk()
main_window.title('Лабораторная работа #2')
main_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
main_window.resizable(width=False, height=False)

main_window.bind('<Button-1>', _entries_init)

main_canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                        background='white')
main_canvas.pack(side='top')

# Центр масштабирования/поворота

center_label = tk.Label(text='Центр масштабирования/поворота', font=15)
center_label.place(x=20, y=820)

center_label_x = tk.Label(text='Xc', font=15)
center_label_x.place(x=60, y=865)

center_label_y = tk.Label(text='Yc', font=15)
center_label_y.place(x=60, y=905)

center_entry_x = tk.Entry(font='Calibri 15', width=10, justify='center')
center_entry_x.place(x=100, y=860)

center_entry_y = tk.Entry(font='Calibri 15', width=10, justify='center')
center_entry_y.place(x=100, y=900)

# Перенос

transfer_label = tk.Label(text='Перенос', font=15)
transfer_label.place(x=490, y=820)

transfer_label_x = tk.Label(text='dX', font=15)
transfer_label_x.place(x=425, y=865)

transfer_label_y = tk.Label(text='dY', font=15)
transfer_label_y.place(x=425, y=905)

transfer_entry_x = tk.Entry(font='Calibri 15', width=10, justify='center')
transfer_entry_x.place(x=465, y=860)

transfer_entry_y = tk.Entry(font='Calibri 15', width=10, justify='center')
transfer_entry_y.place(x=465, y=900)

transfer_button = tk.Button(text='Перенести', font=15,
                            width=11, command=_transfer)
transfer_button.place(x=465, y=940)

# Масштабирование

scale_label = tk.Label(text='Масштабирование', font=15)
scale_label.place(x=760, y=820)

scale_label_x = tk.Label(text='Kx', font=15)
scale_label_x.place(x=715, y=865)

scale_label_y = tk.Label(text='Ky', font=15)
scale_label_y.place(x=715, y=905)

scale_entry_x = tk.Entry(font='Calibri 15', width=12, justify='center')
scale_entry_x.place(x=755, y=860)

scale_entry_y = tk.Entry(font='Calibri 15', width=12, justify='center')
scale_entry_y.place(x=755, y=900)

scale_button = tk.Button(text='Масштабировать', font=15,
                         width=13, command=_scale)
scale_button.place(x=755, y=940)

# Поворот

rotate_label = tk.Label(text='Поворот', font=15)
rotate_label.place(x=1120, y=820)

rotate_entry = tk.Entry(font='Calibri 15', width=12, justify='center')
rotate_entry.place(x=1080, y=860)

rotate_label_phi = tk.Label(text='α', font=20)
rotate_label_phi.place(x=1050, y=865)

rotate_button = tk.Button(text='Повернуть', font=15,
                          width=13, command=_rotate)
rotate_button.place(x=1085, y=940)

# Кнопки отмены и возврата

cancel_button = tk.Button(text='Вернуться в начало', font=15,
                          width=23, command=_cancel_all)
cancel_button.place(x=1400, y=860)

cancel_button = tk.Button(text='Вернуться на один шаг', font=15,
                          width=23, command=_cancel)
cancel_button.place(x=1400, y=910)

_entries_init(None)

_draw_house()

main_window.mainloop()
