import cmath
import math


def task_2():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    P = 2 * (a + b)
    S = a * b
    print(P)
    print(S)


def task_1():
    a = int(input("Enter a"))
    print("P=", 4 * a, "S=".a ** 2)


def task_3():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    c = int(input("Enter c"))
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    print(V)
    print(S)


def task_4():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    print(cmath.sqrt(a * b))


def task_5():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    c = math.sqrt((a ** 2) + (b ** 2))
    p = a + b + c
    print(c)
    print(p)


def task_6():
    A = int(input("Enter A"))
    B = int(input("Enter B"))
    C = int(input("Enter C"))
    A, B, C = B, C, A
    print(A, B, C)


def task_7():
    A = int(input("Enter A"))
    B = int(input("Enter B"))
    C = int(input("Enter C"))
    A, B, C = C, A, B
    print(A, B, C)


def task_8():
    x = int(input("Enter x"))
    y = 3 * (x ** 6) - 6 * (x ** 2) + 7
    print(y)


def task_9():
    x = int(input("Enter x"))
    y = 4 * ((x - 3) ** 6) + 7 * ((x - 2) ** 3) + 2
    print(y)


def task_10():
    name = input("Enter your name: ")
    print("Hello", name)


def task_11():
    sum_num = 0
    num = int(input("Enter num"))
    for digit in num:
        sum_num += int(digit)
    print(sum_num)


def task_12():
    number = int(input("Enter number"))
    D = ((number / 24) / 60) / 60
    H = ((number - (D * 24 * 60 * 60)) / 60) / 60
    S = (number - ((D * 24 * 60 * 60) + (H * 60 * 60)))
    print(D)
    print(H)
    print(S)


def task_13():
    K = int(input("Enter K"))
    day_of_week = (1 + K) % 7
    print("Day of week:", day_of_week)


def task_14():
    num1 = int(input('Enter  num1: '))
    num2 = int(input('Enter  num2'))
    num3 = int(input('Enter num3'))
    print(sorted([num1, num2, num3]))


def task_15():
    number1 = int(input('Enter num1'))
    number2 = int(input('Enter num2'))
    number3 = int(input('Enter num3'))
    number4 = int(input('Enter num4'))
    print(sum([number1, number2, number3, number4]))
    print(number1 - number2 - number3 - number4)
    print(number1 * number2 * number3 * number4)


def task_16():
    x = int(input('Enter  x: '))
    y = int(input("Enter y"))
    print((abs(x) + abs(y)) / (1 + abs(x) * abs(y)))


def task_17():
    a = float(input('Enter  a: '))
    print(a ** 3)
    print(4 * (a ** 2))


def task_18():
    a = float(input('Enter  a: '))
    b = float(input('Enter  b: '))
    print((a + b) / 2)
    print(cmath.sqrt(a * b))


def task_19():
    x = float(input('Enter  x: '))
    y = float(input('Enter'))
    z = float(input('Enter  z: '))
    a = ((cmath.sqrt(abs(x - 1)) - (abs(y)) ** (1 / 3)) / (1 + ((x ** 2) / 2) + (y ** 2) / 2))
    b = x * (cmath.atan(z) + cmath.exp(-(x + 3)))
    print(a)
    print(b)


def task_20():
    x = float(input('Enter  x: '))
    y = float(input('Enter y'))
    z = float(input('Enter  z: '))
    a = ((3 + cmath.exp(y - 1)) / (1 + ((x ** 2) * (abs(y - cmath.tan(z))))))
    b = 1 + abs(y - x) + ((y - x) ** 2) / 2 + ((abs(y - x)) ** 3) / 3
    print(a)
    print(b)


def task_21():
    x = float(input('Enter  x: '))
    y = float(input('Enter y'))
    z = float(input('Enter  z: '))
    a = (1 + y) * (((x + y) / ((x ** 2) + 4)) / cmath.exp(-x - 2) + (1 / ((x ** 2) + 4)))
    b = (1 + cmath.cos(y - 2)) / ((x ** 4) / (2 + (cmath.sin(z)) ** 2))
    print(a)
    print(b)


def task_22():
    x = float(input('Enter  x: '))
    y = float(input('Enter y'))
    z = float(input('Enter  z: '))
    a = y + x / (y ** 2) + (abs((x ** 2) / y + (x ** 3) / 3))
    b = 1 + (cmath.tan(z / 2)) ** 2
    print(a)
    print(b)


def task_23():
    x = int(input())
    y = int(input())
    z = int(input())

    a = 2 * cmath.cos(x - cmath.pi / 6) / (0.5 + cmath.sin(y) ** 2)

    b = 1 + z ** 2 / (3 + z ** 2 / 5)

    print(a)
    print(b)


def task_24():
    x = int(input())
    y = int(input())
    z = int(input())

    a = (1 + cmath.sin(x + y) ** 2) / (2 + abs(x - 2 * x / (1 + x ** 2 * y ** 2))) + x

    b = cmath.cos(cmath.atan(1 / z)) ** 2

    print(a)
    print(b)


def task_25():
    x = int(input())
    y = int(input())
    z = int(input())

    a = cmath.log((y - cmath.sqrt(abs(x))) * (x - y / (z + x ** 2 / 4)))

    b = x - (x ** 2 / math.factorial(3)) + (x ** 5 / math.factorial(5))

    print(a)
    print(b)


def task_32():
    x1 = float(input("Enter x1"))
    x2 = float(input("Enter x2"))
    y1 = float(input("Enter y1"))
    y2 = float(input("Enter y2"))
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print(d)


def task_33():
    x1 = float(input("Enter x1"))
    y1 = float(input("Enter y1"))
    x2 = float(input("Enter x2"))
    y2 = float(input("Enter y2"))
    x3 = float(input("Enter x3"))
    y3 = float(input("Enter y3"))
    AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    AC = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    BC = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    print(AB + AC + BC)
