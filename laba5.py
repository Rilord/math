# Лабораторная работа №5
#
#

x = float(input("Введите начальное значение x:\t"))
n = int(input("Введите первый элемент видимой последовательности:\t"))
s = float(input("Введите шаг:\t"))
eps = float(input("Введите погрешность:\t"))
e = int(input("Введите максимальное количество шагов:\t"))

y = x
S = y
t = 1
print('\n')
print('-'*42)
print("\u2503 {:^14s}\u2503 {:^14s}\u2503" .format
      ("число элементов в суммк", "текущая сумма"))
print('-'*42)

while abs(y) > eps and t <= e:
    if t >= n and t % s == (n % s):
        print("\u2503 {:^23}\u2503 {:^14.7f}\u2503" .format
              (t, S))
    y *= x*x/(2*t)/(2*t+1)
    S += y

    t = t + 1

print('-'*42)
print('\n')

if(t > e):
    print('Ряд не сошелся за {:d}  элементов'.format(e))
elif(t <= e):
    print('Ряд сошелся за {:d} шагов'.format(t-1))
