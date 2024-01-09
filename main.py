import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def parabolic_interpolation(x, y):
    if len(x) != 4 or len(y) != 4:
        raise ValueError("Потрібно ввести рівно 4 точки")

    plt.ion()

    for i in range(10):
        # Розділення точок на два сегменти
        x_left, x_right = x[:3], x[1:]
        y_left, y_right = y[:3], y[1:]

        # Створення функцій інтерполяції для обох сегментів
        f_left = interp1d(x_left, y_left, kind='quadratic')
        f_right = interp1d(x_right, y_right, kind='quadratic')

        # Генерація точок для побудови графіка
        x_vals_left = np.linspace(x_left[0], x_left[2], 100)
        x_vals_right = np.linspace(x_right[0], x_right[2], 100)

        # Розрахунок значень y за допомогою функцій інтерполяції
        y_vals_left = f_left(x_vals_left)
        y_vals_right = f_right(x_vals_right)

        plt.clf()
        plt.scatter(x, y, color='red', label='Точки')
        plt.plot(x_vals_left, y_vals_left, label='Лівий сегмент')
        plt.plot(x_vals_right, y_vals_right, label='Правий сегмент')

        # Отримання точок для усереднення та їх розрахунок
        x_avg_vals = np.linspace(x_vals_left[-1], x_vals_right[0], 100)
        y_avg_left = f_left(x_avg_vals)
        y_avg_right = f_right(x_avg_vals)

        y_avg = (y_avg_left + y_avg_right) / 2

        plt.plot(x_avg_vals, y_avg, 'k--', label='Усереднення точок')

        plt.legend()
        plt.draw()
        plt.pause(5)

        x[0] = float(input("Введіть нове значення x1: "))
        y[0] = float(input("Введіть нове значення y1: "))
        x[-1] = float(input("Введіть нове значення x4: "))
        y[-1] = float(input("Введіть нове значення y4: "))

    plt.ioff()
    plt.show()

x_values = []
y_values = []

for i in range(4):
    x = float(input(f"Введіть x{i + 1}: "))
    y = float(input(f"Введіть y{i + 1}: "))
    x_values.append(x)
    y_values.append(y)

parabolic_interpolation(x_values, y_values)






# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d
#
# def parabolic_interpolation(x, y):
#     if len(x) != 4 or len(y) != 4:
#         raise ValueError("Потрібно ввести рівно 4 точки")
#
#     # Розділення точок на два сегменти
#     x_left, x_right = x[:3], x[1:]
#     y_left, y_right = y[:3], y[1:]
#
#     # Створення функцій інтерполяції для обох сегментів
#     f_left = interp1d(x_left, y_left, kind='quadratic')
#     f_right = interp1d(x_right, y_right, kind='quadratic')
#
#     # Генерація точок для побудови графіка
#     x_vals_left = np.linspace(x_left[0], x_left[2], 100)
#     x_vals_right = np.linspace(x_right[0], x_right[2], 100)
#
#     # Розрахунок значень y за допомогою функцій інтерполяції
#     y_vals_left = f_left(x_vals_left)
#     y_vals_right = f_right(x_vals_right)
#
#     plt.scatter(x, y, color='red', label='Точки')
#     plt.plot(x_vals_left, y_vals_left, label='Лівий сегмент')
#     plt.plot(x_vals_right, y_vals_right, label='Правий сегмент')
#
#     # Отримання точок для усереднення та їх розрахунок
#     x_avg_vals = np.linspace(x_vals_left[-1], x_vals_right[0], 100)
#     y_avg_left = f_left(x_avg_vals)
#     y_avg_right = f_right(x_avg_vals)
#
#     y_avg = (y_avg_left + y_avg_right) / 2
#
#     plt.plot(x_avg_vals, y_avg, 'k--', label='Усереднення точок')
#
#     plt.legend()
#     plt.show()
#
# x_values = []
# y_values = []
#
# for i in range(4):
#     x = float(input(f"Введіть x{i + 1}: "))
#     y = float(input(f"Введіть y{i + 1}: "))
#     x_values.append(x)
#     y_values.append(y)
#
# parabolic_interpolation(x_values, y_values)