import tkinter as tk
import graphics_math as gm
import math
import itertools as it
from tkinter import ttk
import tkinter.messagebox as tmb

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
        tmb.showerror(title='Ошибка!', message='Choose coordinates to delete!')
        return


def change_set():
    global CURRENT_SET

    if CURRENT_SET == 1:
        table_1.place_forget()
        vsb_1.place_forget()
        table_2.place(x=20, y=200)
        vsb_2.place(x=30 + 200 + 2, y=200, height=230)

        change_set_button['text'] = 'Редактировать 1-е множество'

        CURRENT_SET = 2
    else:
        table_2.place_forget()
        vsb_2.place_forget()
        table_1.place(x=20, y=200)
        vsb_1.place(x=30 + 200 + 2, y=200, height=230)

        change_set_button['text'] = 'Редактировать 2-е множество'

        CURRENT_SET = 1


def solve():
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

    gm.draw_circle(0, 0, 1800,
                   main_canvas, 'red')

    number_of_circles = 0

    for coordinates_1 in it.combinations_with_replacement(initial_set_1, 3):
        for coordinates_2 in it.combinations_with_replacement(initial_set_2, 3):
            coordinates_1 = list(coordinates_1)
            coordinates_2 = list(coordinates_2)
            circle_center_1 = gm.get_circle_center(coordinates_1)
            circle_center_2 = gm.get_circle_center(coordinates_2)

            if circle_center_1[0] is None or circle_center_2[0] is None:
                continue
            else:
                number_of_circles += 1

            # radius_1 = gm.get_circle_radius(coordinates_1)
            # radius_2 = gm.get_circle_radius(coordinates_2)

            # gm.draw_circle(circle_center_1[0], circle_center_1[1], radius_1,
            #                main_canvas, 'red')
            # gm.draw_circle(circle_center_2[0], circle_center_2[1], radius_2,
            #                main_canvas, 'green')

            # dot_1 = gm.get_tangent_coordinates(circle_center_1, radius_1,
            #                                    circle_center_2, radius_2)
            #
            # gm.draw_circle(circle_center_1[0], circle_center_1[1], radius_1,
            #                  main_canvas, 'red')
            # gm.draw_circle(circle_center_2[0], circle_center_2[1], radius_2,
            #                  main_canvas, 'red')
            #
            # gm.draw_segment(circle_center_1[0], circle_center_1[1],
            #                   dot_1[0], dot_1[1], main_canvas, 'green')
            # gm.draw_segment(dot_1[0], dot_1[1],
            #                   dot_1[2], dot_1[3], main_canvas, 'green')
            # gm.draw_segment(circle_center_2[0], circle_center_2[1],
            #                   dot_1[2], dot_1[3], main_canvas, 'green')
            # gm.draw_segment(circle_center_1[0], circle_center_1[1],
            #                   circle_center_2[0], circle_center_2[1],
            #                   main_canvas, 'green')


main_form = tk.Tk()
main_form.title('Лабораторная работа #1')
main_form.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+450+350')
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
vsb_1.place(x=30 + 200 + 2, y=200, height=230)
table_1.configure(yscrollcommand=vsb_1.set)

table_2 = ttk.Treeview(main_form, height=10, columns=('x', 'y'),
                       show='headings')
table_2.column("#1", anchor='center', stretch=False, width=100)
table_2.heading('x', text='X')
table_2.column("#2", anchor='center', stretch=False, width=100)
table_2.heading('y', text='Y')

vsb_2 = ttk.Scrollbar(main_form, orient="vertical", command=table_2.yview)
table_2.configure(yscrollcommand=vsb_2.set)

add_entry = tk.Entry(font=15, width=20, justify='center', relief='sunken')
add_entry.place(x=20, y=40)

add_button = tk.Button(text='Добавить точку', command=add_coordinates)
add_button.place(x=20, y=70)

delete_button = tk.Button(text='Удалить точку', command=delete_coordinates)
delete_button.place(x=20, y=100)

read_button = tk.Button(text='Получить решение', command=solve)
read_button.place(x=20, y=130)

change_set_button = tk.Button(text='Редактировать 2-е множество',
                              command=change_set)
change_set_button.place(x=20, y=160)

gm.draw_axes(main_canvas, CANVAS_WIDTH, CANVAS_HEIGHT)

main_form.mainloop()
