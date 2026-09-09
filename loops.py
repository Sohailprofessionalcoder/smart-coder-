#1. n numbers
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(i)

#2. print from n to 1
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(i)

#3.all even numbers
n = int(input("Enter N: "))
for i in range(2, n + 1, 2):
    print(i)

#4.print all odd numbers
n = int(input("Enter N: "))
for i in range(1, n + 1, 2):
    print(i)

#5.sum of all n numbers
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)

    