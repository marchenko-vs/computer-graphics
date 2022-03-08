import tkinter as tk


CANVAS_WIDTH = 450
CANVAS_HEIGHT = 450


root = tk.Tk()
root.geometry('500x500')

cv = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='white')
cv.pack()

x_a = 0
y_a = 0

x_c_1 = -50
y_c_1 = -50
radius_1 = 30

x_c_2 = 50
y_c_2 = 50
radius_2 = 10

k_x_max = CANVAS_WIDTH - 50
k_y_max = CANVAS_HEIGHT - 50

k_x_min = 50
k_y_min = 50

x_max = x_c_2 + radius_2
y_max = y_c_2 + radius_2

x_min = x_c_1 - radius_1
y_min = y_c_1 - radius_1

k_x = (k_x_max - k_x_min) / (x_max - x_min)
k_y = (k_y_max - k_y_min) / (y_max - y_min)

x_k_1 = round(k_x_min + (x_c_1 - x_min) * k_x)
y_k_1 = round(k_y_min + (y_max - y_c_1) * k_y)
radius_1 *= k_x

x_k_2 = round(k_x_min + (x_c_2 - x_min) * k_x)
y_k_2 = round(k_y_min + (y_max - y_c_2) * k_y)
radius_2 *= k_x

x_k_a = round(k_x_min + (x_a - x_min) * k_x)
y_k_a = round(k_y_min + (y_max - y_a) * k_y)

cv.create_oval(x_k_a, y_k_a, x_k_a + 3, y_k_a + 3, fill='red')
cv.create_oval(x_k_1 - radius_1, y_k_1 + radius_1, x_k_1 + radius_1, y_k_1 - radius_1)
cv.create_oval(x_k_2 - radius_2, y_k_2 + radius_2, x_k_2 + radius_2, y_k_2 - radius_2)

root.mainloop()
