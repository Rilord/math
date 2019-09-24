# Лабораторная работа №2 "Треугольник в координатной плоскости"
# ax, ay - A(x, y)
# bx, by - B(x, y)
# cx, cy - C(x, y)
# ab - AB
# bc - BC
# ac - AC
# A1x + B1y + C1 = 0 - Уравнение прямой AB
# A2x + B2y + C2 = 0 - Уравнение прямой BC
# A3x + B3y + C3 = 0  Уравнение прямой AC
# abc - угол ABC
# bac - угол BAC
# bca - угол BCA
# d1 - расстояние от точки до AB
# d2 - расстояние от точки до BC
# d3 - расстояние от точки до AC
# is_AB - Лежит ли точка в полуплоскости, заданной AB
# is_BC - Лежит ли точка в полуплоскости, заданной BC
# is_AC - Лежит ли точка в полуплоскости, заданной AC
# Пример для точек (0, 0), (8, 0), (8, 6) и (6, 2):
#   1. AB = 8, BC = 6 ,AC = 10
#   2. Не Тупоугольный
#   3. Биссектрисса из наименьшего угла - 8.4327
#   4. Точка лежит внутри Треугольника
#   5. Ближайшее расстояние от точки до какой-либо стороны треугольника - 2

from math import sqrt, pow

ax, ay = map(int, input("Введите ax и ay\n").split())
bx, by = map(int, input("Введите bx и by\n").split())
cx, cy = map(int, input("Введите cx и cy\n").split())

ab = sqrt(pow(ax - bx, 2) + pow(ay - by, 2))

bc = sqrt(pow(bx - cx, 2) + pow(by - cy, 2))

ac = sqrt(pow(ax - cx, 2) + pow(ay - cy, 2))

if((ab + bc > ac) and (ab + ac > bc) and (ac + bc > ab)):
    print("AB = {:f}, BC = {:f} и AC = {:f}".format(ab, bc, ac))

    A1 = ay - by
    B1 = bx - ax
    C1 = ax * by - ay * bx

    A2 = by - cy
    B2 = cx - bx
    C2 = bx * cy - by * cx

    A3 = cy - ay
    B3 = ax - cx
    C3 = cx * ay - cy * ax

    bac = (A1 * -A3 + B1 * -B3)/sqrt(A1**2 + B1**2)/sqrt(A3**2 + B3**2)

    abc = (A2 * -A1 + B2 * -B1)/sqrt(A2**2 + B2**2)/sqrt(A1**2 + B1**2)

    bca = (-A3 * A2 + -B3 * B2)/sqrt(A3**2 + B3**2)/sqrt(A2**2 + B2**2)

    if (abc < 0) or (bac < 0) or (bca < 0):
        print("Треугольник тупоугольный")
    else:
        print("Треугольник не тупоугольный")

    if bc <= ac and bc <= ab:
        bs = sqrt(ab * ac * (ab + ac + bc) * (ab + ac - bc))/(ab + ac)
        print("Биссектриса из наименьшего угла равна={:0.7f} ".format(bs))
    elif ac <= bc and ac <= ab:
        bs = sqrt(ab * bc * (ab + ac + bc) * (ab - ac + bc))/(ab + bc)
        print("Биссектриса из наименьшего угла равна={:0.7f} ".format(bs))
    else:
        bs = sqrt(ac * bc * (ab + ac + bc) * (-ab + ac + bc))/(ac + bc)
        print("Биссектриса из наименьшего угла равна={:0.7f} ".format(bs))

    x, y = map(int, input().split())

    is_AB = (ax - x)*(by-ay)-(bx-ax)*(ay-y)
    is_BC = (bx - x)*(cy-by)-(cy-by)*(by-y)
    is_AC = (cx - x)*(ay-cy)-(ax-cx)*(cy-y)

    if ((is_AB >= 0 and is_BC >= 0 and is_AC >= 0) or
            (is_AB <= 0 and is_BC <= 0 and is_AC <= 0)):
        print("Данная точка лежит внутри треугольника")

        d1 = abs(A1 * x + B1 * y + C1)/sqrt(A1**2 + B1**2)
        d2 = abs(A2 * x + B2 * y + C2)/sqrt(A2**2 + B2**2)
        d3 = abs(A3 * x + B3 * y + C3)/sqrt(A3**2 + B3**2)

        if d1 <= d2 <= d3:
            print("Наиближайшее расстояние{:d}: ".format(d1))
        elif d2 <= d1 < d3:
            print(d2)
        else:
            print(d3)
    else:
        print("Данная точка не лежит внутри данного треугольника")
else:
    print("Неправильный треугольник")
# Выполнил Диордиев.К
