# Project created by Piotr Sarna
# import library
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import RANSACRegressor

# Function for read files
def read_file(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for x_cord, y_cord, z_cord in reader:
            yield float(x_cord), float(y_cord), float(z_cord)


# MAIN
if __name__ == '__main__':
    # Value rewrite
    data = []
    for p in read_file('zad1.xyz'):
        data.append(p)

    # Assignment of data to individual axes
    data_x, data_y, data_z = [], [], []
    i = 0
    points = len(data)
    while i < points:
        data_x.append(data[i][0])
        data_y.append(data[i][1])
        data_z.append(data[i][2])
        i = i + 1

    # Initialization RANSAC
    ransac = RANSACRegressor()

    # Initialization figure
    fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # ax.scatter3D(data_x, data_y, data_z)
    plt.scatter(data_x, data_y, color='red')
    plt.show()
