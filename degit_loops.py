#1.count the numbers
n = int(input("Enter a number: "))
count = 0
temp = abs(n)
if temp == 0:
    count = 1
while temp > 0:
    count += 1
    temp //= 10
print("Number of digits:", count)

#2.sum of number digits
n = int(input("Enter a number: "))
temp = abs(n)
total = 0
while temp > 0:
    total += temp % 10
    temp //= 10
print("Sum of digits:", total)

#3.reverse numbers
n = int(input("Enter a number: "))
temp = abs(n)
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if n < 0:
    reversed_num = -reversed_num
print("Reversed number:", reversed_num)

#4.palindrome number
n = int(input("Enter a number: "))
temp = n
reversed_num = 0
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
if n == reversed_num:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")


#5.happy number
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

n = int(input("Enter a number: "))
print(f"{n} is {'a happy' if is_happy(n) else 'not a happy'} number")



#6.product ofdigits
def product_of_digits(n):
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)

n = int(input("Enter a number: "))
print("Product of digits:", product_of_digits(abs(n)))


#7.extract and print
n = int(input("Enter a number: "))
digits = str(abs(n))
for d in digits:
    print(d)