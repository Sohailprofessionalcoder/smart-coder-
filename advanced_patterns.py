### Advanced Patterns (Nested Logic)

**103. Butterfly pattern**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

**104. Hollow diamond inside rectangle**
n = int(input("Enter N (even number recommended): "))
size = 2 * n
for i in range(size):
    for j in range(size):
        dist = abs(i - n) + abs(j - n)
        if dist == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

**105. Number diamond**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

**106. Zigzag pattern**
rows = 3
n = int(input("Enter N (length): "))
matrix = [[0] * n for _ in range(rows)]
row = 0
going_down = True
for col in range(n):
    matrix[row][col] = 1
    if going_down:
        row += 1
        if row == rows:
            row = rows - 2
            going_down = False
    else:
        row -= 1
        if row < 0:
            row = 1
            going_down = True

for r in matrix:
    print(" ".join("*" if v else " " for v in r))


**107. Spiral number matrix (4x4)**
n = 4
matrix = [[0] * n for _ in range(n)]
top, bottom, left, right = 0, n - 1, 0, n - 1
num = 1
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for j in range(right, left - 1, -1):
        matrix[bottom][j] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(" ".join(f"{v:2}" for v in row))

**108. Right arrow pattern**
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * i)


**109. X pattern**
n = int(input("Enter N: "))
for i in range(n):
    for j in range(n):
        if j == i or j == (n - 1 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()


**110. Plus (+) pattern**
n = int(input("Enter N (odd number): "))
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()


**111. Heart shape pattern**
# Uses the heart curve formula: (x^2 + y^2 - 1)^3 - x^2*y^3 <= 0
for y in range(15, -15, -1):
    yy = y / 10
    row = ""
    for x in range(-15, 16):
        xx = x / 10
        val = (xx**2 + yy**2 - 1)**3 - (xx**2) * (yy**3)
        row += "*" if val <= 0 else " "
    print(row)

**112. Square with diagonals marked**
n = int(input("Enter N: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    