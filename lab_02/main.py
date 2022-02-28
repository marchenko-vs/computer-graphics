import math
import tkinter as tk


C = 10
D = 1


def circle_function(x: float, radius: float) -> float:
    return math.sqrt(radius * radius - x * x)


def parabola_function(x: float) -> float:
    global C
    global D

    return C - (x - D) * (x - D)


def draw_circle(a: float, b: float, radius: float, canvas_name):
    canvas_name.create_oval(a - radius, b + radius, a + radius, b - radius)


def draw_parabola(min_limit: float, max_limit: float, canvas_name):
    while min_limit < max_limit:
        y = parabola_function(min_limit)
        canvas_name.create_oval(min_limit + 100, y + 100, min_limit + 100, y + 100)
        min_limit += 0.01


def main():
    main_window = tk.Tk()
    main_window.title('Laboratory work #2')
    main_window.geometry('600x400+350+350')

    main_canvas = tk.Canvas(height=300, width=500, background='white')
    main_canvas.pack()

    draw_circle(50, 50, 10, main_canvas)

    main_window.mainloop()


if __name__ == '__main__':
    main()
