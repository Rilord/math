from math import sin
a, b, c = map(float, input("Введите начало, конец и шаг\n").
              split())

print("\n\n\n")
max1 = a * a
min1 = a * a

a, b, c = int(a * 1000), int(b * 1000), int(c * 1000)

for x in range(a, b + c, c):
    x /= 1000
    f1 = x * x
    if(f1 > max1):
        max1 = f1
    elif(f1 < min1):
        min1 = f1


d = abs(max1 - min1)
z = int((abs(max1/d)*70)) + 1

c_1 = 3
if(max1 > 0 and min1 > 0):
    c_1 = 0
elif(max1 < 0 and min1 < 0):
    c_1 = 1

s1 = ' '*5
s2 = ' '*5
s1 += '{:7.2f}'.format(min1)+' '*63+'{:7.2f}'.format(max1)
s2 += '|'+'-'*70+'|'
print(s1, '\n', s2)
for t in range(a, b+c, c):
    t /= 1000
    f1 = t * t
    d1 = int((abs(f1 - min1)/d)*70)
    if(c_1 == 0):
        print(' '*5 + ' '*d1 + '*' + (86 - d1)*' '+'{:.3f}'.format(t))
    elif(c_1 == 1):
        print(' '*5 + ' '*d1 + '*' + (86 - d1)*' '+'{:.3f}'.format(t))
    else:
        if(d1 < z):
            print(' '*5 + ' '*d1 + '*'+' '*(z-d1)
                  + '|' + ' '*(86-z) + '{:.3f}'.format(t))
        if(d1 > z):
            print(' '*6 + ' '*z
                  + '|'+' '*(d1-z) + '*' + ' '*(85-d1)+'{:.3f}'.format(t))
        elif(d1 == z):
            print(' '*6 + ' '*d1 + 'x' + ' '*(86-d1) + '{:.3f}'.format(t))
