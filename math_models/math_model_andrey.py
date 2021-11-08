def r(coord_x, coord_x2, coord_y, coord_y2): # получает 4 числа. возвращает 1 число. Высчитывает расстояние между 2 точками на плоскости
    return ((coord_x - coord_x2) ** 2 + (coord_y - coord_y2) ** 2) ** 0.5
print('Введите количество тел')
n = int(input()) #количество тел

print('Введите скорости сначала по оси х затем по оси у')
vx = list(map(int, input().split())) #скорости по х
vy = list(map(int, input().split())) #скорости по у

print('Введите координаты сначала по оси х затем по оси у')
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print('Введите массу')
m = list(map(int, input().split()))

ax = [-1] * n
ay = [-1] * n

fx = [-1] * n #возжействия всех тел на рассматриваемое по оси х
fy = [-1] * n #возжействия всех тел на рассматриваемое по оси у

dt = 0.01 #время

sum_f_x = 0 #суммарная сила по х  в некоторый момент времени
sum_f_y = 0 #суммарная сила по у в некоторый момент времени
help_var = 0
while help_var < 10 ** 3:
    for i in range(0, n):
        sum_f_x = 0
        sum_f_y = 0

        #cчитаем силу по х
        for j in range(n):
            if (i != j):
                fx[i] = (x[j] - x[i]) / r(x[i], x[j], y[i], y[j])
                sum_f_x+=fx[i]

        #пересчет значений по х для всех тел
        ax[i] = sum_f_x / m[i]
        vx[i] = vx[i] + ax[i] * dt
        x[i] = x[i] + vx[i] * dt

        # cчитаем силу по y
        for j in range(n):
            if (i != j):
                fy[i] = (y[j] - y[i]) / r(x[i], x[j], y[i], y[j])
                sum_f_y+=fy[i]

        # пересчет значений по у для всех тел
        ay[i] = sum_f_y / m[i]
        vy[i] = vy[i] + ay[i] * dt
        y[i] = y[i] + vy[i] * dt
        print("Тело номер %s имеет координаты" % (i + 1), x[i], 'и', y[i])
    help_var+=1