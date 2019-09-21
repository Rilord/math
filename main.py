from math import sqrt, pow, abs

ax, ay, bx, by, cx, cy = map(int, input().split())

ab = int(sqrt(int(pow(ax - bx, 2) + pow(ay - by, 2))))

bc = int(sqrt(int(pow(bx - cx, 2) + pow(by - cy, 2))))

ac = int(sqrt(int(pow(ax - cx, 2) + pow(ay - cy, 2))))
print(ab, bc, ac)

# Прямая AB
A1 = ay - by
B1 = bx - ax
C1 = ax * by - ay * bx

print("{} and {} and {}".format(A1, B1, C1))
# Прямая BC
A2 = by - cy
B2 = cx - bx
C2 = bx * cy - by * cx
print("{} and {} and {}".format(A2, B2, C2))
# Прямая AC
A3 = cy - ay
B3 = ax - cx
C3 = cx * ay - cy * ax
print("{:d} and {:d} and {:d}".format(A3, B3, C3))
# Угол BAC
bac = (A1 * A2 + B1 * B2)/sqrt(A1**2 + B1**2)/sqrt(A2**2 + B2**2)
print("BAC =: ", bac)
# Угол ABC
abc = (A2 * A3 + B2 * B3)/sqrt(A2**2 + B2**2)/sqrt(A3**2 + B3**2)
print("ABC =: ", abc)
# Угол BCA
bca = (A3 * A1 + B3 * B1)/sqrt(A3**2 + B3**2)/sqrt(A1**2 + B1**2)
print("BCA =: ", bca)
if (abc < 0) or (bac < 0) or (bca < 0):
    print("StupidAngle")
else:
    print("SmartAngle")
if bac < abc < bca:
    bs = int((2 * ab * ac * sqrt((1 - bac)/2))/(ab + ac))
    print(bs)

elif abc < bac < bca:
    bs = int((2 * ab * bc * sqrt((1 - abc)/2))/(ab + bc))
    print(bs)
else:
    bs = int((2 * ac * bc * sqrt((1 - bca)/2))/(ac + bc))
    print(bs)

x, y = map(int, input().split())

if(pow(-1, C1 < 0)(A1 * x + B1 * y + C1 > 0)
    and pow(-1, C2 < 0)(A2 * x + B2 * y + C2 > 0)
        and pow(-1, C3 < 0)(A3 * x + B3 * y + C3 > 0)):
    print("Yup")
    d1 = abs(A1 * x + B1 * y + C1)/sqrt(A1**2 + B1**2)
    d2 = abs(A2 * x + B2 * y + C2)/sqrt(A2**2 + B2**2)
    d3 = abs(A3 * x + B3 * y + C3)/sqrt(A3**2 + B3**2)
    if d1 < d2 < d3:
        print(d1)
    elif d2 < d1 < d3:
        print(d2)
    else:
        print(d3)
