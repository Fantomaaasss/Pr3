# 1
a = float(input("Type in frist digit: "))
b = float(input("Type in second digit: "))
c = float(input("Type in third digit: "))

if a >= 0:
    a = a ** 2
else:
    a = a ** 4

if b >= 0:
    b = b ** 2
else:
    b = b ** 4

if c >= 0:
    c = c ** 2
else:
    c = c ** 4

print("Results of calculations:", a, b, c)

# 2
x1 = float(input("Type in the x1 coordinate for point  A: "))
y1 = float(input("Type in the y1 coordinate for point A: "))
x2 = float(input("Type in the x2 coordinate for point B: "))
y2 = float(input("Type in the y2 coordinate for point B: "))

distance_A = (x1**2 + y1**2) ** 0.5
distance_B = (x2**2 + y2**2) ** 0.5

if distance_A < distance_B:
    print("Point A is closer to origin")
else:
    print("Point B is closer to origin")

# 3
angle1 = float(input("Type in the first angle(in degrees) "))
angle2 = float(input("Type in the second angle(in degrees) "))

angle3 = 180 - (angle1 + angle2)

if angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("This triangle alrteady exist")
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("This triangle is right angled")
    else:
        print("This triangle is not a right triangle")
else:
    print("This triangle does not exist")

# 4
x = float(input("Type in first digit: "))
y = float(input("Type in second digit: "))

if x < y:
    x = (x + y) / 2
    y = x * y * 2
else:
    y = (x + y) / 2
    x = x * y * 2

print("Changed values: x =", x, ", y =", y)

# 5
x = float(input("Type in x coordinatye for point A: "))
y = float(input("Type in y coordinate for point A: "))

if x == 0 and y == 0:
    print("Point is at origin")
elif x == 0:
    print("Point is at Y axel.")
elif y == 0:
    print("Point is at X axel.")
elif x > 0 and y > 0:
    print("Point is at first coordinate angle.")
elif x < 0 and y > 0:
    print("Point is at second coordinate angle.")
elif x < 0 and y < 0:
    print("Point is at third coordinate angle.")
else:
    print("Point is at fourth coordinate angle.")

# 6
a = int(input("Type in first int digit: "))
b = int(input("Type in second int digit: "))

if a != b:
    max_val = max(a, b)
    a = max_val
    b = max_val
else:
    a = 0
    b = 0

print("Changed values: a =", a, ", b =", b)

# 7
a = float(input("Type in first digit: "))
b = float(input("Type in second digit: "))
c = float(input("Type in third digit: "))

negative_count = 0
if a < 0:
    negative_count += 1
if b < 0:
    negative_count += 1
if c < 0:
    negative_count += 1

print("Number of negative numbers", negative_count)

# 8
a = float(input("Type in first digit: "))
b = float(input("Type in second digit: "))
c = float(input("Type in third digit: "))

positive_count = 0
if a > 0:
    positive_count += 1
if b > 0:
    positive_count += 1
if c > 0:
    positive_count += 1

print("Number of positivw digits:", positive_count)

# 9
a = float(input("Type in first digit: "))
b = float(input("Type in second digit: "))
c = float(input("Type in third digit: "))

integer_count = 0
if a.is_integer():
    integer_count += 1
if b.is_integer():
    integer_count += 1
if c.is_integer():
    integer_count += 1

print("Number of integer digits", integer_count)

# 10
a = float(input("Type in first digit: "))
b = float(input("Type in second digit: "))
c = float(input("Type in third digit: "))
k = float(input("Type in k number: "))

if a % k == 0:
    print(f"Number  {k} is divisor of number {a}")
if b % k == 0:
    print(f"Number {k} is divisor of number {b}")
if c % k == 0:
    print(f"Number  {k} is divisor of number {c}")