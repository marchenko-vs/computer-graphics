import tkinter as tk
import os
import graphics_math as gm
import itertools as it
import tkinter.messagebox as tmb

from tkinter import ttk

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

CANVAS_WIDTH = 550
CANVAS_HEIGHT = 450

CURRENT_SET = 1


def add_coordinates():
    if CURRENT_SET == 1:
        tree = table_1
    else:
        tree = table_2

    try:
        coordinates = list(map(float, add_entry.get().split(', ')))
    except ValueError:
        tmb.showerror(title='Ошибка!', message='Некорректный тип данных!')
        return

    if len(coordinates) != 2:
        tmb.showerror(title='Ошибка!', message='Некорректный формат данных!')
        return

    if coordinates not in tree.get_children():
        tree.insert('', tk.END, values=coordinates)


def delete_coordinates():
    if CURRENT_SET == 1:
        tree = table_1
    else:
        tree = table_2

    row_id = tree.focus()
    try:
        tree.delete(row_id)
    except:
        tmb.showerror(title='Ошибка!', message='Не выбрана координата, '
                                               'которую нужно удалить.')
        return


def change_set():
    global CURRENT_SET

    if CURRENT_SET == 1:
        table_1.place_forget()
        vsb_1.place_forget()
        table_2.place(x=20, y=200)
        vsb_2.place(x=230, y=200, height=230)

        change_set_button['text'] = 'Редактировать 1-е множество'

        CURRENT_SET = 2
    else:
        table_2.place_forget()
        vsb_2.place_forget()
        table_1.place(x=20, y=200)
        vsb_1.place(x=230, y=200, height=230)

        change_set_button['text'] = 'Редактировать 2-е множество'

        CURRENT_SET = 1


def solve():
    main_canvas.delete('all')

    initial_set_1 = []
    for line in table_1.get_children():
        tmp = list()
        for value in table_1.item(line)['values']:
            tmp.append(float(value))
        initial_set_1.append(tmp)
        tmp = []

    initial_set_2 = []
    for line in table_2.get_children():
        tmp = list()
        for value in table_2.item(line)['values']:
            tmp.append(float(value))
        initial_set_2.append(tmp)
        tmp = []

    if len(initial_set_1) < 3:
        tmb.showerror(title='Ошибка!', message='Введено менее трех '
                                                         'координат первого множества.')
        return

    if len(initial_set_2) < 3:
        tmb.showerror(title='Ошибка!', message='Введено менее трех '
                                                         'координат второго множества.')
        return

    solution_found = False

    result_area = 0

    result_coordinates_1 = list()
    result_circle_center_1 = list()
    result_radius_1 = 0

    result_coordinates_2 = list()
    result_circle_center_2 = list()
    result_radius_2 = 0

    result_rectangle_coordinates = list()

    for coordinates_1 in it.combinations(initial_set_1, 3):
        for coordinates_2 in it.combinations(initial_set_2, 3):
            coordinates_1 = list(coordinates_1)
            coordinates_2 = list(coordinates_2)

            circle_center_1 = gm.get_circle_center(coordinates_1)
            circle_center_2 = gm.get_circle_center(coordinates_2)

            if circle_center_1[0] is None:
                log_file.write(f'Circles {coordinates_1} does not exits.\n')
                continue

            if circle_center_2[0] is None:
                log_file.write(f'Circles {coordinates_2} does not exits.\n')
                continue

            solution_found = True

            radius_1 = gm.get_circle_radius(coordinates_1)
            radius_2 = gm.get_circle_radius(coordinates_2)

            rectangle_coordinates = \
                gm.get_tangent_coordinates(circle_center_1, radius_1,
                                           circle_center_2, radius_2)

            print(rectangle_coordinates)

            current_area = gm.get_rectangle_area(
                [circle_center_1, circle_center_2,
                 rectangle_coordinates[:2], rectangle_coordinates[2:4]])

            log_file.write(f'Area is {current_area} for circles '
                           f'{coordinates_1} and {coordinates_2}.\n')

            if current_area > result_area:
                result_area = current_area

                result_circle_center_1 = circle_center_1.copy()
                result_radius_1 = radius_1
                result_coordinates_1 = coordinates_1.copy()

                result_circle_center_2 = circle_center_2.copy()
                result_radius_2 = radius_2
                result_coordinates_2 = coordinates_2.copy()

                result_rectangle_coordinates = rectangle_coordinates

    if not solution_found:
        tmb.showinfo(title='Результат.',
                               message='Решение не может быть найдено.')
        return

    gm.draw_axes(main_canvas, CANVAS_WIDTH, CANVAS_HEIGHT)

    gm.draw_circle(result_circle_center_1[0], result_circle_center_1[1],
                   result_radius_1,
                   main_canvas, 'red')
    gm.draw_circle(result_circle_center_2[0], result_circle_center_2[1],
                   result_radius_2,
                   main_canvas, 'red')

    gm.draw_segment(result_circle_center_1[0], result_circle_center_1[1],
                    result_rectangle_coordinates[0],
                    result_rectangle_coordinates[1],
                    main_canvas, 'green')
    gm.draw_segment(result_rectangle_coordinates[0],
                    result_rectangle_coordinates[1],
                    result_rectangle_coordinates[2],
                    result_rectangle_coordinates[3],
                    main_canvas, 'green')
    gm.draw_segment(result_circle_center_2[0], result_circle_center_2[1],
                    result_rectangle_coordinates[2],
                    result_rectangle_coordinates[3],
                    main_canvas, 'green')
    gm.draw_segment(result_circle_center_1[0], result_circle_center_1[1],
                    result_circle_center_2[0], result_circle_center_2[1],
                    main_canvas, 'green')

    log_file.write(f'The largest area is {result_area} for circles '
                   f'{result_coordinates_1} and {result_coordinates_2}.\n')

    tk.messagebox.showinfo(title='Результат.',
                           message=f'Самая большая площадь {result_area} для '
                                   f'окружностей {result_coordinates_1} и '
                                   f'{result_coordinates_2}.')


try:
    log_file = open('logs\\log.txt', 'w')
except FileNotFoundError:
    os.system('mkdir logs')
    log_file = open('logs\\log.txt', 'w')

main_form = tk.Tk()
main_form.title('Лабораторная работа #1')
main_form.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+1100+300')
main_form.resizable(width=False, height=False)

style = ttk.Style()
style.theme_use('clam')

main_canvas = tk.Canvas(main_form, width=CANVAS_WIDTH,
                        height=CANVAS_HEIGHT, bg='white')
main_canvas.pack(side='right')

table_1 = ttk.Treeview(main_form, height=10, columns=('x', 'y'),
                       show='headings')
table_1.column("#1", anchor='center', stretch=False, width=100)
table_1.heading('x', text='X')
table_1.column("#2", anchor='center', stretch=False, width=100)
table_1.heading('y', text='Y')
table_1.place(x=20, y=200)

vsb_1 = ttk.Scrollbar(main_form, orient="vertical", command=table_1.yview)
vsb_1.place(x=230, y=200, height=230)
table_1.configure(yscrollcommand=vsb_1.set)

table_2 = ttk.Treeview(main_form, height=10, columns=('x', 'y'),
                       show='headings')
table_2.column("#1", anchor='center', stretch=False, width=100)
table_2.heading('x', text='X')
table_2.column("#2", anchor='center', stretch=False, width=100)
table_2.heading('y', text='Y')

vsb_2 = ttk.Scrollbar(main_form, orient="vertical", command=table_2.yview)
table_2.configure(yscrollcommand=vsb_2.set)

add_entry = tk.Entry(font=15, width=22, justify='center', relief='sunken')
add_entry.place(x=20, y=40)

add_button = tk.Button(text='Добавить точку', command=add_coordinates, width=27)
add_button.place(x=20, y=70)

delete_button = tk.Button(text='Удалить точку', command=delete_coordinates,
                          width=27)
delete_button.place(x=20, y=100)

read_button = tk.Button(text='Получить решение', command=solve, width=27)
read_button.place(x=20, y=130)

change_set_button = tk.Button(text='Редактировать 2-е множество',
                              command=change_set, width=27)
change_set_button.place(x=20, y=160)

main_form.mainloop()

log_file.close()
