num = int(input("Введите целое число К"))
b = set()
print('Повторяющиеся элементы')
while num > 0:
    t = num % 10
    b.add(t)
    if (t not in b):
        b.add(t)
    elif (t in b) and ((-t - 1) not in b):
        b.discard(t)
        b.add(-t - 1)
        print(t)

    num //= 10
print(b)
