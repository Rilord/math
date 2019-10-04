from math import log10, exp
a, b, c = map(float, input("Enter lower limit and upper limit\n").
              split())
num = int(input("Enter number of wtpuxob\n"))
print("\n\n\n")
max1 = a*log10(a)+0.125
min1 = a*log10(a)+0.125
max2 = 3*a - exp(a)
min2 = 3*a - exp(a)

a, b, c = int(a * 1000), int(b * 1000), int(c * 1000)

for x in range(a, b + c, c):
    x /= 1000
    f1 = x*log10(x)+0.125
    if(f1 > max1):
        max1 = f1
    elif(f1 < min1):
        min1 = f1
    f2 = 3 * x - exp(x)
    if(f2 > max2):
        max2 = f2
    elif(f2 < min2):
        min2 = f2

mx = max(max1, max2)
mn = float(min(min1, min2))
d = abs(mx - mn)
z = int((abs(mn/d)*70))
s1 = ' '*12
s2 = ' '*12
m = 70//num
k = (d / 70) * m
bg = mn
for i in range(1, m * num, m):
    s1 += '╩' + "═"*(m-2)
    s2 += "{:.2f}".format(bg) + ' '*(m-6)
    bg += k
print(s2)
print(s1 + '\n')
for t in range(a, b+c, c):
    t /= 1000
    f1 = t*log10(t)+0.125
    d1 = int((abs(f1 - mn)/d)*70)
    f2 = 3 * t - exp(t)
    d2 = int((abs(f2 - mn)/d)*70)
    if(d1 > d2):
        d3 = d1-d2

        out = ' ' * d2 + '*' + ' '*d3 + '!'
        out = out[:z-2] + '║' + out[z-1:]
        print("{:7.3f}".format(t) + ' '*5 + out)
    elif(d2 > d1):
        d3 = d2 - d1
        out = ' ' * d1 + '*' + ' '*d3 + '!'
        out = out[:z-2] + '║' + out[z-1:]
        print("{:7.3f}".format(t) + ' '*5 + out)
