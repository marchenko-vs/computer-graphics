import graphics_math as gm
import math

from constants import *


class Plus:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates.copy()

    def draw(self, canvas_size: list, color: str, canvas_name):
        gm.draw_line([self.coordinates[0], self.coordinates[2]],
                     canvas_size, color, canvas_name)
        gm.draw_line([self.coordinates[1], self.coordinates[3]],
                     canvas_size, color, canvas_name)

    def transfer(self, canvas_size: list,
                 entry_d_x_name, entry_d_y_name, canvas_name):
        d_x = float(entry_d_x_name.get())
        d_y = float(entry_d_y_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.transfer_point(self.coordinates[i][0],
                                                    self.coordinates[i][1],
                                                    d_x, d_y)

    def scale(self, canvas_size: list,
              entry_k_x_name, entry_k_y_name,
              entry_x_c_name, entry_y_c_name, canvas_name):
        k_x = float(entry_k_x_name.get())
        k_y = float(entry_k_y_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.scale_point(self.coordinates[i][0],
                                                 self.coordinates[i][1],
                                                 k_x, k_y, x_c, y_c)

    def rotate(self, canvas_size: list, entry_phi_name,
               entry_x_c_name, entry_y_c_name, canvas_name):
        phi = float(entry_phi_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.rotate_point(self.coordinates[i][0],
                                                  self.coordinates[i][1],
                                                  phi, x_c, y_c)


class Rectangle:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates.copy()

    def draw(self, canvas_size: list, color: str, canvas_name):
        gm.draw_line([self.coordinates[0], self.coordinates[1]],
                     canvas_size, color, canvas_name)
        gm.draw_line([self.coordinates[1], self.coordinates[2]],
                     canvas_size, color, canvas_name)
        gm.draw_line([self.coordinates[2], self.coordinates[3]],
                     canvas_size, color, canvas_name)
        gm.draw_line([self.coordinates[0], self.coordinates[3]],
                     canvas_size, color, canvas_name)

    def transfer(self, canvas_size: list,
                 entry_d_x_name, entry_d_y_name, canvas_name):
        d_x = float(entry_d_x_name.get())
        d_y = float(entry_d_y_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.transfer_point(self.coordinates[i][0],
                                                    self.coordinates[i][1],
                                                    d_x, d_y)

    def scale(self, canvas_size: list,
              entry_k_x_name, entry_k_y_name,
              entry_x_c_name, entry_y_c_name, canvas_name):
        k_x = float(entry_k_x_name.get())
        k_y = float(entry_k_y_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.scale_point(self.coordinates[i][0],
                                                 self.coordinates[i][1],
                                                 k_x, k_y, x_c, y_c)

    def rotate(self, canvas_size: list, entry_phi_name,
               entry_x_c_name, entry_y_c_name, canvas_name):
        phi = float(entry_phi_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.rotate_point(self.coordinates[i][0],
                                                  self.coordinates[i][1],
                                                  phi, x_c, y_c)


class Triangle:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates.copy()

    def draw(self, canvas_size: list, color: str, canvas_name):
        gm.draw_line([self.coordinates[0], self.coordinates[1]],
                     canvas_size, color, canvas_name)
        gm.draw_line([self.coordinates[1], self.coordinates[2]],
                     canvas_size, color, canvas_name)
        gm.draw_line([self.coordinates[0], self.coordinates[2]],
                     canvas_size, color, canvas_name)

    def transfer(self, canvas_size: list,
                 entry_d_x_name, entry_d_y_name, canvas_name):
        d_x = float(entry_d_x_name.get())
        d_y = float(entry_d_y_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.transfer_point(self.coordinates[i][0],
                                                    self.coordinates[i][1],
                                                    d_x, d_y)

    def scale(self, canvas_size: list,
              entry_k_x_name, entry_k_y_name,
              entry_x_c_name, entry_y_c_name, canvas_name):
        k_x = float(entry_k_x_name.get())
        k_y = float(entry_k_y_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.scale_point(self.coordinates[i][0],
                                                 self.coordinates[i][1],
                                                 k_x, k_y, x_c, y_c)

    def rotate(self, canvas_size: list, entry_phi_name,
               entry_x_c_name, entry_y_c_name, canvas_name):
        phi = float(entry_phi_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(len(self.coordinates)):
            self.coordinates[i] = gm.rotate_point(self.coordinates[i][0],
                                                  self.coordinates[i][1],
                                                  phi, x_c, y_c)


class Oval:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates
        self.polygon_coordinates = gm.poly_oval(self.coordinates[0][0],
                                                self.coordinates[0][1],
                                                self.coordinates[1][0],
                                                self.coordinates[1][1])

    def draw(self, canvas_size: list, color: str, canvas_name):
        tmp = self.polygon_coordinates.copy()

        for i in range(0, len(tmp) - 1, 2):
            tmp[i] += canvas_size[0] / 2
            tmp[i + 1] = -tmp[i + 1] + canvas_size[1] / 2

        canvas_name.create_polygon(tuple(tmp),
                                   fill='white',
                                   outline=color)

    def rotate(self, canvas_size: list, entry_phi_name,
               entry_x_c_name, entry_y_c_name, canvas_name):
        phi = float(entry_phi_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(0, len(self.polygon_coordinates) - 1, 2):
            tmp = gm.rotate_point(self.polygon_coordinates[i],
                                  self.polygon_coordinates[i + 1],
                                  phi, x_c, y_c)

            self.polygon_coordinates[i] = tmp[0]
            self.polygon_coordinates[i + 1] = tmp[1]

    def transfer(self, canvas_size: list,
                 entry_d_x_name, entry_d_y_name, canvas_name):
        d_x = float(entry_d_x_name.get())
        d_y = float(entry_d_y_name.get())

        for i in range(0, len(self.polygon_coordinates) - 1, 2):
            tmp = gm.transfer_point(self.polygon_coordinates[i],
                                    self.polygon_coordinates[i + 1],
                                    d_x, d_y)

            self.polygon_coordinates[i] = tmp[0]
            self.polygon_coordinates[i + 1] = tmp[1]

    def scale(self, canvas_size: list,
              entry_k_x_name, entry_k_y_name,
              entry_x_c_name, entry_y_c_name, canvas_name):
        k_x = float(entry_k_x_name.get())
        k_y = float(entry_k_y_name.get())

        x_c = float(entry_x_c_name.get())
        y_c = float(entry_y_c_name.get())

        for i in range(0, len(self.polygon_coordinates) - 1, 2):
            tmp = gm.scale_point(self.polygon_coordinates[i],
                                 self.polygon_coordinates[i + 1],
                                 k_x, k_y, x_c, y_c)

            self.polygon_coordinates[i] = tmp[0]
            self.polygon_coordinates[i + 1] = tmp[1]
