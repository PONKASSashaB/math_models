print("Введите число тел")

# Число тел. Целое положительное
n = int(input())

# Вводим  x, y, Vx, Vy и m и задаем Fy, Fx, Ay, Ax. Все - массивы чисел
print("Введите x, y, Vx, Vy и m. Числа вводите на отдельных строках для каждой переменной. Числа для одной переменной и разных тел вводите на одной строке")
x = list(map(int, input().split()))
y = list(map(int, input().split()))
Ax = [-1] * n
Fx = [-1] * n
Vx = list(map(int, input().split()))
Vy = list(map(int, input().split()))
Ay = [-1] * n
Fy = [-1] * n
m = list(map(int, input().split()))

# Время пересчета. Число
dt = 0.01

if (len(x) != n or len(y) != n or len(Vx) != n or len(Vy) != n or len(m) != n):
    print("Ты не смог ввести правильное количество чисел. Ты - дно. Ты - днище. Ты пирожок с ничем. Ты - никто. Ты - пыль на сапогоах гения, создавшего этот код")
else:

    j = 0
    while j <= 10**3:
        for i in range (0, n):
            Fx[i] = 10
            Ax[i] = Fx[i] / m[i]
            Vx[i] = Vx[i] + Ax[i] * dt
            x[i] = x[i] + Vx[i] * dt

            Fy[i] = 10
            Ay[i] = Fy[i] / m[i]
            Vy[i] = Vy[i] + Ay[i] * dt
            y[i] = y[i] + Vy[i] * dt

            print("Тело номер %s имеет координаты" % (i + 1), x[i], 'и', y[i])
        j+=1
