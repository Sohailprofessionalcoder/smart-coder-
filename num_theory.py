#1.factorial
n = int(input("Enter N: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

#2.prime number
n = int(input("Enter a number: "))
is_prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(f"{n} is {'prime' if is_prime else 'not prime'}")

#3.all the number are prime
n = int(input("Enter N: "))
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

#4.GCD
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y:
    x, y = y, x % y
print("GCD:", x)


#5.LCM
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

lcm = (a * b) // gcd(a, b)
print("LCM:", lcm)