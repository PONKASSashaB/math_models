
# получает 4 числа. возвращает 1 число. Высчитывает расстояние между 2 точками на плоскости
def r(coord_x, coord_x2, coord_y, coord_y2):
    return ((coord_x - coord_x2) ** 2 + (coord_y - coord_y2) ** 2) ** 0.5

'''
    получает кооординаты (тела по рассматривемой оси, рассматриваемое тело по той же оси, аналогично для оставшийся оси) и кол-во тел.
    возвращает силу по данной координате, с которой все тела действуют на выбранное
'''
def count_f (coordS_first, our_coord_first, coordS_second, our_coord_second, n):
    sum_f = 0
    fx = []
    for i in range(n):
        if (r(coordS_second[i], our_coord_second, coordS_first[i], our_coord_first) != 0):
            fx.append(-(our_coord_first - coordS_first[i]) / r(coordS_second[i], our_coord_second, coordS_first[i], our_coord_first))
            sum_f += fx[len(fx) - 1]
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

# количество тел
print('Введите количество тел')
n = int(input())

print('Введите скорости сначала по оси х затем по оси у')

# скорости по х
vx = list(map(int, input().split()))

# скорости по у
vy = list(map(int, input().split()))

print('Введите координаты сначала по оси х затем по оси у')
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print('Введите массу')
m = list(map(int, input().split()))

ax = [-1] * n
ay = [-1] * n

# воздействия всех тел на рассматриваемое по оси х и у
fx = [-1] * (n - 1)
fy = [-1] * (n - 1)

# время между пересчетами
dt = 0.01

# время с начала работы модели
t = 0

while t < 100:
    for i in range(0, n):

        # пересчет значений по х для всех тел
        ax[i] = count_a(count_f(x, x[i], y, y[i], n), m[i])
        vx[i] = count_v(vx[i], ax[i], dt)
        x[i] = count_coord(x[i], vx[i], dt)

        # пересчет значений по у для всех тел
        ay[i] = count_a(count_f(y, y[i], x, x[i], n), m[i])
        vy[i] = count_v(ay[i], ay[i], dt)
        y[i] = count_coord(y[i], vy[i], dt)

        if ((t * 10) % 10 == 0):
            print("Тело номер %s имеет координаты" % (i + 1), x[i], 'и', y[i])

    t+=dt