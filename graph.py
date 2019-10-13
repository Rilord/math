
a, b, c = map(float, input("Enter lower limit and upper limit\n").
              split())

print("\n\n\n")
max1 = a*a - 4
min1 = a*a - 4


a, b, c = int(a * 1000), int(b * 1000), int(c * 1000)

for x in range(a, b + c, c):
    x /= 1000
    f1 = x * x - 4
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
    c_2 = 1

s1 = ' '*12
s2 = ' '*12


for t in range(a, b+c, c):
    t /= 1000
    f1 = t * t - 4
    d1 = int((abs(f1 - max1)/d)*70) + 1
    if(c_1 == 0):
        print(' '*5 + ' '*d1 + '*' + ' '*(80-d1) + '{:4.3}'.format(t))
    elif(c_1 == 1):
        print(' '*5 + ' '*d1 + '*' + ' '*(80-d1) + '{:4.3}'.format(t))
    else:
        if(d1 < z):
            print(' '*5 + ' '*d1 + '*'+' '*(z-d1)
                  + '|' + ' '*(80-z) + '{:4.3}'.format(t))
        if(d1 > z):
            print(' '*5 + ' '*z + '|'+' '*(d1-z) + '*'
                  + ' '*(80-d1) + '{:4.3}'.format(t))
        elif(d1 == z):
            print(' '*5 + ' '*d1 + 'x'
                  + ' '*(80-z) + '{:4.3f}'.format(t))
