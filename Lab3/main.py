import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np

def push(stack, pixel):
    stack.append(pixel)

def pop(stack):
    return stack.pop()

def fill_pixel_and_plot(x, y, fill_pixel, stack, image, ax):
    if image[y, x] == 0:
        fill_pixel.add((x, y))
        stack.append((x, y))
        rect = Rectangle((x - 0.5, y - 0.5), 1, 1, linewidth=0.5, edgecolor='red', facecolor='red')
        ax.add_patch(rect)
        plt.draw()
        plt.pause(0.1)
        image[y, x] = 1

def fill_row(x, y, image, fill_pixel, stack, ax):
    x_right = x + 1
    while x_right < 32 and image[y, x_right] != 1:
        x_right += 1

    x_left = x - 1
    while x_left >= 0 and image[y, x_left] != 1:
        x_left -= 1

    for i in range(x_left + 1, x_right):
        fill_pixel_and_plot(i, y, fill_pixel, stack, image, ax)

def plot_boundary_fill(polygons, seed=None, title="Многокутники"):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))

    image_size = 32
    image = np.zeros((image_size, image_size), dtype=int)

    for polygon in polygons:
        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]
            points_on_line = bresenham_line(x1, y1, x2, y2)
            for point in points_on_line:
                image[point[1], point[0]] = 1

    for point in np.argwhere(image == 1):
        rect = Rectangle((point[1] - 0.5, point[0] - 0.5), 1, 1, linewidth=0.5, edgecolor='red', facecolor='red')
        ax.add_patch(rect)
    ax.set_xlim(0, image_size)
    ax.set_ylim(0, image_size)

    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))

    plt.grid(True)
    plt.show(block=False)

    if seed is None:
        print("Будь ласка, виберіть точку на графіку.")
        seed = plt.ginput(1, show_clicks=True, timeout=0)
        seed = [tuple(map(lambda x: round(x), seed[0]))]
        print("Використовується вибрана точка: {}".format(seed))
        if not seed:
            print("Ви не вибрали точку. Завершення програми.")
            plt.close()
            return
        seed = (int(seed[0][0]), int(seed[0][1]))
    else:
        print("Використовується задана точка: {}".format(seed))

    seed = (4, 20)
    fill_pixel = set()
    stack = [seed]

    x, y = seed
    fill_pixel_and_plot(x, y, fill_pixel, stack, image, ax)

    while stack:
        x, y = pop(stack)
        fill_row(x, y, image, fill_pixel, stack, ax)

        if y + 1 < image_size and image[y + 1, x] == 0:
            fill_row(x, y + 1, image, fill_pixel, stack, ax)

        if y - 1 >= 0 and image[y - 1, x] == 0:
            fill_row(x, y - 1, image, fill_pixel, stack, ax)

    plt.close()
    print(fill_pixel)


def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

polygon1 = [(4, 4), (4, 26), (20, 26), (28, 18), (21, 4), (21, 8), (10, 8), (10, 4)]
polygon2 = [(10, 12), (10, 20), (17, 20), (21, 16), (21, 12)]
plot_boundary_fill([polygon1, polygon2])





