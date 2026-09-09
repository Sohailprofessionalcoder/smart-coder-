
#1.switch case
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

match op:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '*':
        print("Result:", a * b)
    case '/':
        print("Result:", a / b if b != 0 else "Error: division by zero")
    case _:
        print("Invalid operator")


#2.month
month = int(input("Enter month number (1-12): "))
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                  7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if month in days_in_month:
    print(f"Days: {days_in_month[month]}")
else:
    print("Invalid month")


#3.posi / negative 
n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")


#4.ascending order
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    first = a
    second, third = (b, c) if b <= c else (c, b)
elif b <= a and b <= c:
    first = b
    second, third = (a, c) if a <= c else (c, a)
else:
    first = c
    second, third = (a, b) if a <= b else (b, a)

print(f"Ascending order: {first}, {second}, {third}")


#5.discriminent
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real roots: {root1:.2f}, {root2:.2f}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One repeated real root: {root:.2f}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print(f"Complex roots: {real:.2f} + {imag:.2f}i, {real:.2f} - {imag:.2f}i")