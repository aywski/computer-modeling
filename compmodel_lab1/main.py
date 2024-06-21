import matplotlib.pyplot as plt
import numpy as np

f = lambda x: np.arctan(x)/(1+x**3)

a = 1 # 1
b = 3 # Inf (sys.maxsize, np.Infinity)

e = 1e-4

x = np.arange(a, b, e)
y = f(x)

#Функція для заміни змінної
u = lambda x: np.sqrt(x)

def integrate_by_trapezoidal(f, a, b, n):
    """Обчислює інтеграл функції f на інтервалі від a до b методом обрізання границь з n прямокутниками.

    Args:
        f: Підінтегральна функція.
        a: Ліва межа інтегрування.
        b: Права межа інтегрування.
        n: Кількість прямокутників.

    Returns:
        Приблизне значення інтеграла.
    """

    h = (b - a) / n

    s = 0
    for i in range(n):
        x0 = a + h*i
        x1 = x0 + h
        sh = (f(x0) + f(x1)) * h / 2
        s += sh
    return s


def newton_integration(f, a, b, n):
  """
  Інтегрування Ньютона

  Аргументи:
    f: функція, яку потрібно інтегрувати
    a: нижня межа інтегрування
    b: верхня межа інтегрування
    n: кількість інтервалів

  Повертає:
    значення інтеграла
  """

  h = (b - a) / n
  x = np.linspace(a, b, n)
  y = f(x)
  sum_of_areas = 0
  for i in range(n):
    sum_of_areas += h * y[i]
  return sum_of_areas

def integration(method, f, a, b, e):
    n0 = 100
    s = method(f, a, b, n0)

    loop = True
    while loop :
        n1 = n0*2
        s0 = s
        s = method(f, a, b, n1)
        delta = abs(s - s0)
        if delta <= e:
            loop = False
        else:
            n0 = n1
    return s

print("\n\n\n")
print("Методом обрізання границь з n прямокутниками:", integration(integrate_by_trapezoidal, f, a, b, e), "\n") # Для нескінченності?
print("Метод Ньютона:", integration(newton_integration, f, a, b, e), "\n")

plt.title("Інтеграл I = arctan(x)dx/(1+x^3)")
plt.plot(x, y)
plt.show()