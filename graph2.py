from math import log10, exp
a, b, c = map(float, input("Enter lower limit and upper limit\n").
              split())
num = int(input("Enter number of wtpuxob\n"))
print("\n\n\n")
max1 = a*log10(a)+0.125
min1 = a*log10(a)+0.125


a, b, c = int(a * 1000), int(b * 1000), int(c * 1000)

for x in range(a, b + c, c):
    x /= 1000
    f1 = x*log10(x)+0.125
    if(f1 > max1):
        max1 = f1
    elif(f1 < min1):
        min1 = f1


d = abs(max1 - min1)
z = int((abs(min1/d)*70))

s1 = ' '*11
s2 = ' '*11
m = 70//num
k = (d / 70) * m
bg = min1
for i in range(1, m * num, m):
    s1 += '╩' + "═"*(m-2)
    s2 += "{:.2f}".format(bg) + ' '*(m-6)
    bg += k
print(s2)
print(s1 + '╩' + '\n')
if(min1 < 0):

    for t in range(a, b+c, c):
        t /= 1000
        f1 = t*log10(t)+0.125
        d1 = int((abs(f1 - min1)/d)*70)

        if z > d1:
            print("{:.3f}".format(t) + ' '*5 +
                  ' '*d1 + '*' + ' '*(z-d1)+'|')
        else:
            print("{:.3f}".format(t) + ' '*6 +
                  ' '*z + '|' + ' ' * (d1-z) + '*')

else:
    for t in range(a, b+c, c):
        t /= 1000
        f1 = t*log10(t)+0.125
        d1 = int((abs(f1 - min1)/d)*70)

        print("{:.3f}".format(t) + ' '*5 + ' ' * d1 + '*')
