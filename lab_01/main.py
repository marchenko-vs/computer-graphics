import graphics_math as gm
import interface as inf
import itertools as it
import os
import tkinter as tk
import tkinter.messagebox as tmb

from tkinter import ttk

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CANVAS_WIDTH = 950
CANVAS_HEIGHT = 700

PADDING = 15

CURRENT_SET = 1

TO_CHANGE = False


def error_handler(number: int, coordinates_1: list, coordinates_2: list):
    if number == 1:
        tmb.showinfo(title='Решение не найдено',
                     message='Точки с координатами {} расположены на '
                             'одной прямой.\n'.format(coordinates_1))
    if number == 2:
        tmb.showinfo(title='Решение не найдено',
                     message='Точки с координатами {} расположены на '
                             'одной прямой.\n'.format(coordinates_2))
    if number == 3:
        tmb.showinfo(title='Решение не найдено',
                     message='Окружность с координатами {} расположена '
                             'внутри окружности с координатами '
                             '{}.\n'.format(coordinates_1, coordinates_2))
    if number == 4:
        tmb.showinfo(title='Решение не найдено',
                     message='Окружность с координатами {} расположена '
                             'внутри окружности с координатами '
                             '{}.\n'.format(coordinates_2, coordinates_1))


def add_coordinate():
    if CURRENT_SET == 1:
        tree = table_1
    else:
        tree = table_2

    coordinates = inf.parse_coordinate(add_entry.get())

    if coordinates[0] is None:
        tmb.showerror(title='Ошибка!', message='Некорректный тип данных!')
        return

    if len(coordinates) != 2:
        tmb.showerror(title='Ошибка!', message='Некорректный формат данных!')
        return

    if coordinates not in tree.get_children():
        tree.insert('', tk.END, values=coordinates)


def change_coordinate():
    global TO_CHANGE

    if CURRENT_SET == 1:
        tree = table_1
    else:
        tree = table_2

    coordinate = inf.parse_coordinate(add_entry.get())

    if coordinate[0] is None:
        tmb.showerror(title='Ошибка!', message='Некорректный тип данных!')
        return

    if len(coordinate) != 2:
        tmb.showerror(title='Ошибка!', message='Некорректный формат данных!')
        return

    row_id = tree.focus()

    tree.delete(row_id)
    tree.insert('', tk.END, values=coordinate)

    change_button['text'] = 'Изменить точку'

    TO_CHANGE = False


def change_row():
    global TO_CHANGE

    if TO_CHANGE:
        change_coordinate()
        return

    if CURRENT_SET == 1:
        tree = table_1
    else:
        tree = table_2

    row_id = tree.focus()

    if row_id == '':
        tmb.showerror(title='Ошибка!', message='Не выбрана координата, '
                                               'которую нужно изменить.')
        return

    TO_CHANGE = True

    coordinate = tree.item(row_id)['values']
    input_str = ', '.join(coordinate)
    add_entry.delete(0, 'end')
    add_entry.insert(0, input_str)

    change_button['text'] = 'Применить изменения'


def enter_handler(event):
    add_coordinate()


def delete_coordinate():
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
        table_2.place(x=20, y=270)
        vsb_2.place(x=285, y=270, height=230)

        change_set_button['text'] = 'Редактировать 1-е множество'

        CURRENT_SET = 2
    else:
        table_2.place_forget()
        vsb_2.place_forget()
        table_1.place(x=20, y=270)
        vsb_1.place(x=285, y=270, height=230)

        change_set_button['text'] = 'Редактировать 2-е множество'

        CURRENT_SET = 1


def solve():
    # initial_set_1 = []
    # for line in table_1.get_children():
    #     tmp = list()
    #
    #     for value in table_1.item(line)['values']:
    #         tmp.append(float(value))
    #
    #     initial_set_1.append(tmp)
    #     tmp = []
    #
    # initial_set_2 = []
    # for line in table_2.get_children():
    #     tmp = list()
    #
    #     for value in table_2.item(line)['values']:
    #         tmp.append(float(value))
    #
    #     initial_set_2.append(tmp)
    #     tmp = []

    initial_set_2 = [[-50, -70], [-30, 10], [50, -30]]
    initial_set_1 = [[150, 39], [200, -30], [230, 20]]

    if len(initial_set_1) < 3:
        tmb.showerror(title='Ошибка!', message='Введено менее трех '
                                               'координат первого множества.')
        return

    if len(initial_set_2) < 3:
        tmb.showerror(title='Ошибка!', message='Введено менее трех '
                                               'координат второго множества.')
        return

    solution_found = False

    cases_counted = 0

    error_code = 0

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
            cases_counted += 1

            coordinates_1 = list(coordinates_1)
            coordinates_2 = list(coordinates_2)

            # Проверка на то, что точки не лежат на одной прямой

            if gm.on_one_line(coordinates_1):
                log_file.write('Точки с координатами {} расположены на '
                               'одной прямой.\n'.format(coordinates_1))
                error_code = 1
                continue

            if gm.on_one_line(coordinates_2):
                log_file.write('Точки с координатами {} расположены на '
                               'одной прямой.\n'.format(coordinates_2))
                error_code = 2
                continue

            # Вычисление координат центров окружностей

            circle_center_1 = gm.get_circle_center(coordinates_1)
            circle_center_2 = gm.get_circle_center(coordinates_2)

            # Вычисление значений радиусов окружностей

            radius_1 = gm.get_circle_radius(circle_center_1, coordinates_1[0])
            radius_2 = gm.get_circle_radius(circle_center_2, coordinates_2[0])

            if gm.circle_in_circle(circle_center_1, radius_1,
                                   circle_center_2, radius_2):
                log_file.write('Окружность с координатами {} расположена '
                               'внутри окружности с координатами '
                               '{}.\n'.format(coordinates_1, coordinates_2))
                error_code = 3
                continue

            if gm.circle_in_circle(circle_center_2, radius_2,
                                   circle_center_1, radius_1):
                log_file.write('Окружность с координатами {} расположена '
                               'внутри окружности с координатами '
                               '{}.\n'.format(coordinates_2, coordinates_1))
                error_code = 4
                continue

            # Вычисление координат двух точек касательных

            rectangle_coordinates = gm.get_tangent_coordinates(circle_center_1,
                                                               radius_1,
                                                               circle_center_2,
                                                               radius_2)

            # Вычисление площади четырехугольника

            current_area = gm.get_rectangle_area(
                [circle_center_1, circle_center_2,
                 rectangle_coordinates[:2], rectangle_coordinates[2:4]])

            solution_found = True

            log_file.write('Площадь четырехугольника равна {:.2f} для '
                           'окружностей с координатами '
                           '{} и {}.\n'.format(current_area, coordinates_1,
                                               coordinates_2))

            if current_area > result_area:
                result_area = current_area

                result_circle_center_1 = circle_center_1.copy()
                result_radius_1 = radius_1
                result_coordinates_1 = coordinates_1.copy()

                result_circle_center_2 = circle_center_2.copy()
                result_radius_2 = radius_2
                result_coordinates_2 = coordinates_2.copy()

                result_rectangle_coordinates = rectangle_coordinates

    log_file.write('Было рассмотрено {} случаев.\n'.format(cases_counted))

    if not solution_found:
        error_handler(error_code, coordinates_1, coordinates_2)
        return

    main_canvas.delete('all')

    critical_points = gm.get_critical_points(result_circle_center_1,
                                             result_radius_1,
                                             result_circle_center_2,
                                             result_radius_2)

    k = gm.get_scale_coefficient(
        [PADDING, PADDING, CANVAS_WIDTH - PADDING, CANVAS_HEIGHT - PADDING],
        critical_points)

    gm.draw_circle(result_circle_center_1[0], result_circle_center_1[1],
                   result_radius_1, critical_points[0], critical_points[3], k,
                   main_canvas, 'red', 1)
    gm.draw_circle(result_circle_center_2[0], result_circle_center_2[1],
                   result_radius_2, critical_points[0], critical_points[3], k,
                   main_canvas, 'red', 1)

    gm.draw_axes([0, 0, CANVAS_WIDTH, CANVAS_HEIGHT], critical_points[0],
                 critical_points[3], k, main_canvas, 'black', 1)

    gm.draw_segment(result_circle_center_1[0], result_circle_center_1[1],
                    result_rectangle_coordinates[0],
                    result_rectangle_coordinates[1], critical_points[0],
                    critical_points[3], k,
                    main_canvas, 'green', 1)
    gm.draw_segment(result_rectangle_coordinates[0],
                    result_rectangle_coordinates[1],
                    result_rectangle_coordinates[2],
                    result_rectangle_coordinates[3], critical_points[0],
                    critical_points[3], k,
                    main_canvas, 'green', 1)
    gm.draw_segment(result_circle_center_2[0], result_circle_center_2[1],
                    result_rectangle_coordinates[2],
                    result_rectangle_coordinates[3], critical_points[0],
                    critical_points[3], k,
                    main_canvas, 'green', 1)
    gm.draw_segment(result_circle_center_1[0], result_circle_center_1[1],
                    result_circle_center_2[0], result_circle_center_2[1],
                    critical_points[0], critical_points[3], k, main_canvas,
                    'green', 1)

    log_file.write('Наибольшая площадь прямоугольника - {:.2f} для окружностей,'
                   ' проходящих через точки с координатами {} и '
                   '{}.\n'.format(result_area, result_coordinates_1,
                                  result_coordinates_2))

    result_circle_center_1[0] = round(result_circle_center_1[0], 2)
    result_circle_center_1[1] = round(result_circle_center_1[1], 2)

    result_circle_center_2[0] = round(result_circle_center_2[0], 2)
    result_circle_center_2[1] = round(result_circle_center_2[1], 2)

    tk.messagebox.showinfo(title='Результат',
                           message='Наибольшая площадь прямоугольника - {:.2f} '
                                   'для окружностей, проходящих через точки с '
                                   'координатами {} и {}.\nЦентры первой и '
                                   'второй окружностей {} и {} соответственно.'
                                   '\nРадиусы {:.2f} и {:.2f}.\nБыло рассмотрено {} '
                                   'различных '
                                   'случаев.\n'.format(result_area,
                                                       result_coordinates_1,
                                                       result_coordinates_2,
                                                       result_circle_center_1,
                                                       result_circle_center_2,
                                                       result_radius_1,
                                                       result_radius_2,
                                                       cases_counted))


try:
    log_file = open('logs/log.txt', 'w', encoding='utf-8')
except FileNotFoundError:
    os.system('mkdir logs')
    log_file = open('logs/log.txt', 'w')

main_form = tk.Tk()
main_form.title('Лабораторная работа #1')
main_form.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+100+100')
main_form.resizable(width=False, height=False)

style = ttk.Style()
style.theme_use('clam')

main_canvas = tk.Canvas(main_form, width=CANVAS_WIDTH,
                        height=CANVAS_HEIGHT, bg='white')
main_canvas.pack(side='right')

table_1 = ttk.Treeview(main_form, height=10, columns=('x', 'y'),
                       show='headings')
table_1.column("#1", anchor='center', stretch=False, width=130)
table_1.heading('x', text='X')
table_1.column("#2", anchor='center', stretch=False, width=130)
table_1.heading('y', text='Y')
table_1.place(x=20, y=270)

vsb_1 = ttk.Scrollbar(main_form, orient="vertical", command=table_1.yview)
vsb_1.place(x=285, y=270, height=230)
table_1.configure(yscrollcommand=vsb_1.set)

table_2 = ttk.Treeview(main_form, height=10, columns=('x', 'y'),
                       show='headings')
table_2.column("#1", anchor='center', stretch=False, width=130)
table_2.heading('x', text='X')
table_2.column("#2", anchor='center', stretch=False, width=130)
table_2.heading('y', text='Y')

vsb_2 = ttk.Scrollbar(main_form, orient="vertical", command=table_2.yview)
table_2.configure(yscrollcommand=vsb_2.set)

add_entry = tk.Entry(width=20, justify='center', relief='sunken',
                     font='Calibri 15 bold')
add_entry.place(x=20, y=30)
add_entry.bind('<Return>', enter_handler)

add_button = tk.Button(text='Добавить точку', command=add_coordinate, width=25,
                       font=15)
add_button.place(x=20, y=70)

delete_button = tk.Button(text='Удалить точку', command=delete_coordinate,
                          width=25, font=15)
delete_button.place(x=20, y=110)

change_button = tk.Button(text='Изменить точку', command=change_row,
                          width=25, font=15)
change_button.place(x=20, y=150)

change_set_button = tk.Button(text='Редактировать 2-е множество',
                              command=change_set, width=25, font=15)
change_set_button.place(x=20, y=190)

read_button = tk.Button(text='Получить решение', command=solve, width=25,
                        font=15)
read_button.place(x=20, y=230)

task = tk.Label(text='На плоскости заданы два\nмножества точек. Найти пару\n'
                'окружностей, каждая из которых\nпроходит хотя бы через три\n'
                'различные точки одного и\nтого же множества, для которой\n '
                'площадь четырехугольника,\nобразованного центрами\nокружностей'
                ' и точками касания\nобщей внешней\nкасательной, максимальна.',
                font=10, width=30)
task.place(x=20, y=500)

main_form.mainloop()

log_file.close()
