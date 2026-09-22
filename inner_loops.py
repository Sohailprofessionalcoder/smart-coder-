**78. Right-angled triangle (stars)**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print("*" * i)

**79. Inverted right-angled triangle**
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print("*" * i)

**80. Right-aligned triangle**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

**81. Inverted right-aligned triangle**
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

**82. Pyramid (centered)**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

**83. Inverted pyramid**
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

**84. Diamond shape**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

**85. Hollow rectangle**
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end="")
        else:
            print(" ", end="")
    print()


**86. Hollow right-angled triangle**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

**87. Sandglass / Hourglass**
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

### Number Patterns

**88. Number triangle (row-wise)**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(str(i) * i)

**89. Sequential number triangle**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))

**90. Floyd's triangle**
n = int(input("Enter number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

**91. 1-0 alternating triangle**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(1 if j % 2 != 0 else 0, end=" ")
    print()

**92. Pascal's triangle**
n = int(input("Enter number of rows: "))
for i in range(n):
    value = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()

**93. Number pyramid (centered)**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


**94. Inverted number triangle**
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(" ".join(str(j) for j in range(1, i + 1)))

**95. Column-wise incrementing**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, end=" ")
    print()

**96. Reverse number triangle**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end=" ")
    print()

**97. Binary number triangle**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()