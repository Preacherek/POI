# Project created by Piotr Sarna
# import library
import random
import math
import matplotlib.pyplot as plt


# Points class
class Point:
    # Method class for points
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z


# Surfaces class
class Surface:
    # Method class for surfaces
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.corner_1 = p1
        self.corner_2 = p2
        self.corner_3 = p3
        self.corner_4 = p4


def surface_hor(min_value_x, max_value_x, min_value_y, max_value_y, z_value, points):
    i = 0
    x_table, y_table, z_table = [], [], []
    while i < points:
        x_table.append(random.uniform(min_value_x, max_value_x))
        y_table.append(random.uniform(min_value_y, max_value_y))
        z_table.append(z_value)
        i = i + 1
    return x_table, y_table, z_table


def surface_ver(min_value_x, max_value_x, min_value_z, max_value_z, y_value, points):
    i = 0
    x_table, y_table, z_table = [], [], []
    while i < points:
        x_table.append(random.uniform(min_value_x, max_value_x))
        y_table.append(y_value)
        z_table.append(random.uniform(min_value_z, max_value_z))
        i = i + 1
    return x_table, y_table, z_table


def make_circle(radius, x_center, y_center):
    r = radius * math.sqrt(random.random())
    theta = 2 * math.pi * random.random()
    return x_center + r * math.cos(theta), y_center + r * math.sin(theta)

def surface_cyl(min_value_x, min_value_y, radius, min_value_z, max_value_z, points):
    i = 0
    x_table, y_table, z_table = [], [], []
    while i < points:
        xp, yp = make_circle(radius, min_value_x, min_value_y)
        x_table.append(xp)
        y_table.append(yp)
        z_table.append(random.uniform(min_value_z, max_value_z))
        i = i + 1
    return x_table, y_table, z_table


# MAIN
if __name__ == '__main__':
    x_data_a, y_data_a, z_data_a = surface_hor(0, 50, 20, 30, 25, 500)
    x_data_b, y_data_b, z_data_b = surface_ver(0, 50, 0, 80, 50, 500)
    x_data_c, y_data_c, z_data_c = surface_cyl(0, 0, 10, 0, 100, 10000)

    # Initialization figure
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(x_data_a, y_data_a, z_data_a)
    ax.scatter3D(x_data_b, y_data_b, z_data_b)
    ax.scatter3D(x_data_c, y_data_c, z_data_c)
    plt.show()

    # xyz_file = open("zad2.xyz", 'w')
    # for i in range(1000):
    #   xyz_file.write("{}\t {}\t {}\t\n".format(x_data_c, y_data_c, z_data_c))

    print("Hello")
