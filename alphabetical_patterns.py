### Alphabet Patterns

**98. Alphabet triangle (row repeat)**
n = int(input("Enter N: "))
for i in range(n):
    print(chr(65 + i) * (i + 1))

**99. Alphabet triangle (sequential)**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


**100. Reverse alphabet triangle**
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


**101. Right-aligned alphabet triangle**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


**102. Alphabet pyramid (centered)**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()