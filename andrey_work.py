# прорисовка
from tkinter import *

# функция sleep для более приятной глазу прорисовки
from time import *

# получает 4 числа. возвращает 1 число. высчитывает расстояние между 2 точками на плоскости
def r(coord_x, coord_x2, coord_y, coord_y2):
    return ((coord_x - coord_x2) ** 2 + (coord_y - coord_y2) ** 2) ** 0.5

'''
    получает кооординаты (тела по рассматривемой оси, рассматриваемое тело по той же оси, аналогично для оставшийся оси), кол-во тел, начальные расстояние между ними и константу k
    возвращает силу по данной координате, с которой все тела действуют на выбранное (сила упругости)
'''

def count_f (coordS_first, our_coord_first, coordS_second, our_coord_second, n, array_r, k):
    sum_f = 0
    f = []
    for i in range(n):
        real_r = r(coordS_second[i], our_coord_second, coordS_first[i], our_coord_first)
        if (real_r != 0):
            f.append(k * (real_r - array_r[i]) * (our_coord_first - coordS_first[i]) / real_r)
            sum_f += f[len(f) - 1]
    return sum_f

#  получает старую скорость, ускорение и время. возвращает новую скорость
def count_v(old_v, a, time):
    return old_v + a * time

# получает силу и массу. возвращает ускорение
def count_a(f, m):
    return f / m

# получает скорость, старую координату и время. возвращает координату
def count_coord(start_coord, v, t):
    return v * t + start_coord

# получает координаты тела и его номер. Выводит и графически отображает(в виде круга с диаметром 4) их
def create_body(x, y, i):
    print("тело номер %s имеет координаты" % (i + 1), x, 'и', y)

    # рисует встроенной функцией круг
    canvas.create_oval(int(x + 1) + 2, int(y + 1) + 2, int(x + 1) - 2, int(y + 1) - 2, fill='black')

'''
Программа моделирует и визуализирует движение тел (материальных точек), выводя их координаты после каждого пересчета на экран.
Тела взаимодействуют друг с другом согласно силе упрогости и изначально расположены в виде квадратной матрицы из n элементов
'''

# создаем экран
root = Tk()
canvas = Canvas(root, width = 800, height = 800, bg = 'white')
canvas.pack()

# количество тел, точный квадрат
print('введите количество тел')
n = 4

print('введите скорости сначала по оси х затем по оси у')

# скорости по х
vx = [0, 0, 0, 0]

# скорости по у
vy = [0, 0, 0, 0]

# расстояние между соседними телами в сетке
print("введите расстояние между телами сначала по горизонтали, затем по вертикали в разных строках")
xs = 3
ys = 3

# координаты левого верхнего тела вс сетке
print('введите координаты левого верхнего тела в одной строке')
x0, y0 = 400, 400

# массы всех тел
print('введите массы')
m = [5, 5, 5, 5]

# ускорения всех тел по 2 осям
ax = [-1] * n
ay = [-1] * n

x = []
y = []

# квадратный корень из n
cr = int((n ** 0.5))

# генерируем начальные координаты тел
for i in range(0, n):
    x.append(-1)
    y.append(-1)
    x[i] = (x0 + (((i + 1) % cr) * xs))
    y[i] = (y0 + (((i + 1) // cr) * ys))

# массив начальных расстояний
array_r = [[-1] * n] * n
for i in range(0, n):
    for j in range(i, n):
        array_r[i][j] = r(x[i], x[j], y[i], y[j])
        array_r[j][i] = array_r[i][j]

# воздействие всех тел на рассматриваемое по оси х и у
fx = [-1] * (n - 1)
fy = [-1] * (n - 1)

# время между пересчетами
dt = 0.02

# время с начала работы модели
t = 0

# константа упрогости
k = 0.01

# моделирование работает, пока время, прошедшие с начала работы модели, меньше определенного порога. В одном шаге цикла
# пересчитываем значения ускорения, скорости и координат для всех тел
while t < 100:

    canvas.create_rectangle(0, 800, 800, 0, fill = 'white')

    # пересчитываем все тела
    for i in range(0, n):

        # пересчет значений ускорения, координаты и скорости по х для всех тел
        ax[i] = count_a(count_f(x, x[i], y, y[i], n, array_r[i], k), m[i])
        vx[i] = count_v(vx[i], ax[i], dt)
        x[i] = count_coord(x[i], vx[i], dt)

        # пересчет значений ускорения, координаты и скорости по у для всех тел
        ay[i] = count_a(count_f(y, y[i], x, x[i], n, array_r[i], k), m[i])
        vy[i] = count_v(vy[i], ay[i], dt)
        y[i] = count_coord(y[i], vy[i], dt)

        # визуализируем движение точек
        create_body(x[i], y[i], i)
    root.update()
    t += dt
root.mainloop()
