import tkinter as tk
import tkinter.colorchooser as clrchs

from constants import *


def _draw_line():
    main_canvas.create_line(50, 50, 100, 100, fill=CURRENT_COLOR)


def _choose_color():
    global CURRENT_COLOR

    CURRENT_COLOR = clrchs.askcolor()[1]


main_window = tk.Tk()
main_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
main_window.title('Лабораторная работа #3')
main_window.resizable(width=False, height=False)

color_chooser_button = tk.Button(text='Выбрать цвет', command=_choose_color)
color_chooser_button.place(x=30, y=30)

draw_line_button = tk.Button(text='Нарисовать отрезок', command=_draw_line)
draw_line_button.place(x=30, y=70)

radio_buttons = tk.Radiobutton()
radio_buttons.place(x=30, y=110)

main_canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                        background='white')
main_canvas.pack(side='right')

main_window.mainloop()

