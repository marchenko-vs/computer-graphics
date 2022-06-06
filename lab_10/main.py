import constants as const
import draw
import tkinter as tk

main_window = tk.Tk()
main_window.title("Лабораторная работа #10")
main_window.geometry(f"{const.WINDOW_WIDTH}x{const.WINDOW_HEIGHT}+0+0")
main_window.resizable(False, False)

main_canvas = tk.Canvas(main_window, width=const.CANVAS_WIDTH, height=const.CANVAS_HEIGHT, bg="white")
main_canvas.pack(side='right')

tk.Label(text="Цвет", font=("Calibri", 20, "bold")).place(width=445, y=10)

color_var = tk.IntVar()
color_var.set(1)

tk.Radiobutton(text="Черный", variable=color_var, value=0,
               font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=60)

tk.Radiobutton(text="Красный", variable=color_var, value=1,
               font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=90)

tk.Radiobutton(text="Синий", variable=color_var, value=2,
               font=("Calibri", 18), anchor="w").place(width=120, height=25, x=40, y=120)

tk.Radiobutton(text="Зеленый", variable=color_var, value=3,
               font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=60)

tk.Radiobutton(text="Желтый", variable=color_var, value=4,
               font=("Calibri", 18), anchor="w").place(width=120, height=25, x=260, y=90)

tk.Radiobutton(text="Фиолетовый", variable=color_var, value=5,
               font=("Calibri", 18), anchor="w").place(width=160, height=25, x=260, y=120)

tk.Label(text="Функция", font=("Calibri", 20, "bold")).place(width=445, y=150)

function_var = tk.IntVar()
function_var.set(0)

tk.Radiobutton(text="sin(x) * cos(z)", variable=function_var, value=0,
               font=("Calibri", 18), anchor="w").place(height=25, x=130, y=190)

tk.Radiobutton(text="sin(cos(x)) * sin(z)", variable=function_var, value=1,
               font=("Calibri", 18), anchor="w").place(height=25, x=130, y=220)

tk.Radiobutton(text="cos(x) * z / 4", variable=function_var, value=2,
               font=("Calibri", 18), anchor="w").place(height=25, x=130, y=250)

tk.Radiobutton(text="cos(x) * cos(sin(z))", variable=function_var, value=3,
               font=("Calibri", 18), anchor="w").place(height=25, x=130, y=280)

tk.Label(text="Пределы", font=("Calibri", 20, "bold")).place(width=445, height=25, y=320)

tk.Label(text="от\tдо\tшаг", font=("Calibri", 18)).place(width=445, y=350)

tk.Label(text="Ox", font=("Calibri", 18)).place(height=25, x=20, y=390)
tk.Label(text="Oz", font=("Calibri", 18)).place(height=25, x=20, y=440)

entry_x_begin = tk.Entry(font=("Calibri", 18), justify='center')
entry_x_begin.place(width=80, height=30, x=80, y=390)

entry_x_end = tk.Entry(font=("Calibri", 18), justify='center')
entry_x_end.place(width=80, height=30, x=175, y=390)

entry_x_step = tk.Entry(font=("Calibri", 18), justify='center')
entry_x_step.place(width=80, height=30, x=280, y=390)

entry_z_begin = tk.Entry(font=("Calibri", 18), justify='center')
entry_z_begin.place(width=80, height=30, x=80, y=440)

entry_z_end = tk.Entry(font=("Calibri", 18), justify='center')
entry_z_end.place(width=80, height=30, x=175, y=440)

entry_z_step = tk.Entry(font=("Calibri", 18), justify='center')
entry_z_step.place(width=80, height=30, x=280, y=440)

tk.Label(text="Масштабирование", font=("Calibri", 20, "bold")).place(width=445, height=25, y=480)

tk.Label(text="Коэффициент", font=("Calibri", 18)).place(x=50, y=510)

entry_scale = tk.Entry(font=("Calibri", 18), justify='center')
entry_scale.place(width=120, height=30, x=250, y=515)

tk.Button(text="Масштабировать", font=("Calibri", 18),
          command=lambda: draw.scale_function(
              entry_scale, main_canvas, color_var, function_var,
              entry_x_begin, entry_x_end, entry_x_step,
              entry_z_begin, entry_z_end, entry_z_step)).place(width=370, height=50, x=40, y=550)

tk.Label(text="Поворот", font=("Calibri", 20, "bold")).place(width=445, y=610)

tk.Label(text="Ox", font=("Calibri", 18)).place(height=30, x=25, y=670)
tk.Label(text="Oy", font=("Calibri", 18)).place(height=30, x=25, y=725)
tk.Label(text="Oz", font=("Calibri", 18)).place(height=30, x=25, y=780)

entry_x_rotate = tk.Entry(font=("Calibri", 18), justify='center')
entry_x_rotate.place(width=125, height=50, x=100, y=660)

entry_y_rotate = tk.Entry(font=("Calibri", 18), justify='center')
entry_y_rotate.place(width=125, height=50, x=100, y=715)

entry_z_rotate = tk.Entry(font=("Calibri", 18), justify='center')
entry_z_rotate.place(width=125, height=50, x=100, y=770)

tk.Button(text="Повернуть", font=("Calibri", 18),
          command=lambda: draw.rotate_x(
              entry_x_rotate, main_canvas, color_var, function_var,
              entry_x_begin, entry_x_end, entry_x_step,
              entry_z_begin, entry_z_end, entry_z_step)). \
    place(width=125, height=50, x=285, y=660)

tk.Button(text="Повернуть", font=("Calibri", 18),
          command=lambda: draw.rotate_y(
              entry_y_rotate, main_canvas, color_var, function_var,
              entry_x_begin, entry_x_end, entry_x_step,
              entry_z_begin, entry_z_end, entry_z_step)). \
    place(width=125, height=50, x=285, y=715)

tk.Button(text="Повернуть", font=("Calibri", 18),
          command=lambda: draw.rotate_z(
              entry_z_rotate, main_canvas, color_var, function_var,
              entry_x_begin, entry_x_end, entry_x_step,
              entry_z_begin, entry_z_end, entry_z_step)). \
    place(width=125, height=50, x=285, y=770)

tk.Button(text="Построить", font=("Calibri", 18),
          command=lambda: draw.build_function(
              main_canvas, color_var, function_var,
              entry_x_begin, entry_x_end, entry_x_step,
              entry_z_begin, entry_z_end, entry_z_step, new_graph=True)). \
    place(width=370, height=50, x=40, y=880)

tk.Button(text="Очистить экран", font=("Calibri", 18),
          command=lambda: draw.clear_canvas(main_canvas)).place(width=370, height=50, x=40, y=935)

entry_x_begin.insert(0, "-10")
entry_x_end.insert(0, "10")
entry_x_step.insert(0, "0.2")

entry_z_begin.insert(0, "-10")
entry_z_end.insert(0, "10")
entry_z_step.insert(0, "0.2")

entry_scale.insert(0, "50")

entry_x_rotate.insert(0, "20")
entry_y_rotate.insert(0, "20")
entry_z_rotate.insert(0, "20")

main_window.mainloop()
