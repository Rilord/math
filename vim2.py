
def Left():
    s = open("sample.txt", 'r+')
    t = []
    i = 1
    ws = 0

    for line in s:
        if i == 1:
            for j in line:
                if j == ' ':
                    ws += 1
                else:
                    break
            i = 0
        t.append(line.strip())

    s.close()

    s = open("sample.txt", 'w')

    for i in t:
        s.write(' ' * ws + i + '\n')

    s.close()


def Right():
    s = open("sample.txt", 'r+')
    t = []
    mx = 0
    for line in s:
        if len(line) > mx:
            mx = len(line)

        t.append(line)

    s.close()

    s = open("sample.txt", 'w')
    for k in t:
        s.write(' '*(mx - len(k) + 1) + k)


def Center():
    m = 0
    s = open("sample.txt", 'r')
    t = 0
    k = 0
    lines = []
    for line in s:
        lc = line
        if len(line) > m:
            m = len(line)
            t = 0
            k = 0
            while lc[k] == ' ':
                if lc[k] == ' ':
                    t += 1
                    k += 1
        lines.append(lc.strip())
    s.close()
    s = open("sample.txt", 'w')

    s.write('')
    s.close()
    for j in range(len(lines)):
        k = list(lines[j])
        while len(''.join(k)) < m:
            for i in range(len(k)):
                if len(''.join(k)) < m and ' ' in k[i]:
                    k[i] = k[i] + ' '

        lines[j] = ''.join(k)
    print(lines)
    s = open("sample.txt", 'w')
    for j in lines:
        s.write(' '*t + j + '\n')
    s.close()


def Calculate():
    ans = []
    s = open("sample.txt", 'r+')
    for line in s:
        linec = line
        count = 0
        ch = 0
        while linec[ch] != '\n':
            while True:
                if linec[ch] in '1234567890':
                    count = 1
                if lines[ch] in '+-' and count = 1:
                    a = ch
                    b = ch
                    k = ''
                    e = ''
                    break

    s.close()


Calculate()
