import numpy as np
import matplotlib.pyplot as plt

def dydx(y, x, k, ys):
    return -k * (y - ys)

def euler(k, x0, y0, ys, h, N):
    """ Метод Ейлера
    Args: 
        k: Параметр диференціального рівняння. - 1
        x0: Початкова точка x. - 0
        y0: Початкова точка y. - 2
        ys: Точка перетину ys. - 1
        h: Крок інтегрування. - 0.1
        N: Кількість кроків інтегрування. - 20

    Returns:
        Масив розв'язку диференціального рівняння.
    """
    y = np.zeros(N + 1)
    y[0] = y0
    for i in range(1, N + 1):
        y[i] = y[i - 1] + dydx(y[i - 1], x0 + i * h, k, ys) * h
    return y

def modified_euler(k, x0, y0, ys, h, N):
    """ Модифікований метод Ейлера
    Args:
        k: Параметр диференціального рівняння.
        x0: Початкова точка x.
        y0: Початкова точка y.
        ys: Точка перетину ys.
        h: Крок інтегрування.
        N: Кількість кроків інтегрування.

    Returns:
        Масив розв'язку диференціального рівняння.
    """
    y = np.zeros(N + 1)
    y[0] = y0
    for i in range(1, N + 1):
        k1 = dydx(y[i - 1], x0 + (i - 1) * h, k, ys)
        k2 = dydx(y[i - 1] + k1 * h, x0 + i * h, k, ys)
        y[i] = y[i - 1] + (k1 + k2) * h / 2
    return y



k = float(input("Введіть параметр k: "))
x0 = float(input("Введіть початкову точку x0: "))
y0 = float(input("Введіть початкову точку y0: "))
ys = float(input("Введіть точку перетину ys: "))
h = float(input("Введіть крок h: "))
N = int(input("Введіть кількість кроків N: "))
print("\n\n\n")

y_euler = euler(k, x0, y0, ys, h, N)
y_modified_euler = modified_euler(k, x0, y0, ys, h, N)
ysarr = [ys] * N

# Малюємо графіки розв'язків
plt.plot(y_euler, label="Метод Ейлера")
plt.plot(y_modified_euler, label="Модифікований метод Ейлера")
plt.plot(ysarr, linestyle = "dashed", label="Вісь перетину")


print("Метод Ейлера:", y_euler[-1], "\n")
print("Модифікований метод Ейлера:", y_modified_euler[-1], "\n")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
