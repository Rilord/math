# From the beggining we create an input of initial values
# all values are separated by ' ' and '\n'
# In sorting we find max length of all values and expanding them
# to that value


def Sort(name):
    with open(name, 'r') as fin:
        data = fin.read().splitlines(True)
    header = data[0]
    with open(name, 'w') as fout:
        fout.writelines(data[1:])
    s = open(name, 'r+')
    nums = 0
    nump = 0
    for line in s:
        nums += 1
        linecopy = line
        linecopy.strip('\n')
        arr = linecopy.split()
        nump = len(arr)
    s.close()
    table = [[' ' for i in range(nump)] for x in range(nums)]
    i = 0
    s = open(name, 'r+')
    for line1 in s:
        linecopy1 = line1
        linecopy1.strip('\n')
        arr1 = linecopy1.split()
        for j in range(nump):
            table[i][j] = arr1[j]
        i += 1
    s.close()
    for i in range(nump):
        for k in range(nums):
            for j in range(nums - 1 - k):
                if table[j][i].isnumeric() is True:
                    if int(table[j][i]) > int(table[j + 1][i]):
                        t = table[j]
                        table[j] = table[j+1]
                        table[j+1] = t
                else:
                    if ord(table[j][i][0]) > ord(table[j + 1][i][0]):
                        t = table[j]
                        table[j] = table[j+1]
                        table[j+1] = t

    s = open(name, 'r+')
    s.truncate(0)
    s.close()
    s = open(name, 'a')
    s.write("".join(header))
    for j in table:
        s.write(" ".join(j) + '\n')
    s.close()


def Search_1(name, num, ex):
    s = open(name, 'r')
    i = 1
    for line in s:
        if '#' not in line:
            res = line
            res.strip('\n')
            m = res.split()
            if m[num - 1] == ex:
                print(str(i) + ' Найденная запись:\n\n')
                print(line)
                i += 1

    s.close()


def Search_2(name, num1, num2, ex1, ex2):
    s = open(name, 'r')
    i = 1
    for line in s:
        if '#' not in line:
            res = line
            res.strip('\n')
            m = res.split()
            if m[num1 - 1] == ex1 and m[num2 - 1] == ex2:
                print(str(i) + ' Найденная запись:\n\n')
                print(line)
                i += 1
    s.close()


def field_it(nump, name, t):

    num = int(input("Введите количество наборов\n"))
    m = [[0 for i in range(nump)] for j in range(num)]

    for i in range(num):
        k = [0] * nump
        for j in range(nump):
            n = "Введите значение в " + str(j + 1) + " поле " + str(i + 1) + " набора\t\n"
            k[j] = input(n)
            m[i][j] = k[j]
    s = open(name, t)
    for a in m:
        res = ''
        for j in range(nump):
            res += a[j] + ' '
        res += '\n'
        s.write(res)
    s.close()
    return num


def Print(name):
    f = open(name, 'r')
    print(f.read())
    f.close()


def menu():
    num = 0
    name = input('Введите название файла:\t\n')

    choice = '0'
    while(choice != '6'):
        choice = input('Введите номер действия:\n\
            1 - создать новый набор записей\n\
            2 - вывод всех записей\n\
            3 - добавить новые записи\n\
            4 - поиск по одному полю\n\
            5 - поиск по двум полям\n\
            7 - сортировать\n\
            6 - выйти\n')

        if(choice == '1'):

            nump = int(input('Введите количество полей\
             для создания набора\t\n'))

            names = [0] * nump
            for j in range(nump):
                names[j] = input("Введите название " + str(j + 1) + " поля\n\t")

            s = open(name, 'w')
            s.write('# ' + " ".join(names) + ' #' + '\n')
            s.close()
            num += field_it(nump, name, 'a')

        elif(choice == '6'):
            print('\nработа завершена')

        elif(choice == '3'):
            nump = int(input('Введите количество полей\
             для добавления записей\n\t'))
            num += field_it(nump, name, 'a')

        elif(choice == '2'):
            s = open(name, 'r')
            Print(name)

        elif(choice == '4'):
            Sort(name)
            s = open(name, 'r')
            j = 0
            for i in s:
                if '#' not in i:
                    j += 1

            num = int(input("Введите номер поля:\t\n"))
            ex = input("Введите значение поля:\t\n")
            Search_1(name, num, ex)

        elif(choice == '5'):
            Sort(name)
            s = open(name, 'r')
            num1, num2 = map(int, input(
                "Введите номера двух полей по которым\
                 нужно производить поиск\n\n\t ").split())
            ex1, ex2 = map(str, input(
                "Введите значения для двух введенных полей соответственно\
                \n\n\t ").split())
            Search_2(name, num1, num2,  ex1, ex2)
        elif(choice == '7'):
            Sort(name)


menu()
