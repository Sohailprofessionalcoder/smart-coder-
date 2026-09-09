#1.greater
a = int(input("enter a :"))
b = int(input("enter b :"))

if a>b :
    print("a is greater")
else:
    print("b is greater ")
    
#2.number check
n = int(input("enter n :"))
if n>0:
    print("n is positive ")
elif n == 0 :
    print("n is zero ")
else:
    print("n is negative")
    
#3.equality check
c = int(input("enter c :"))
if a==b and a == c:
    print("the three values are equal")
    
#4.eligibilty
age = int(input("enter age :"))
if age >= 18 :
    print("voting eligible ")
else:
    print("voting not eligible")

#5.char check
U_C = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
L_C = ('abcdefghijklmnopqrstuvwxyz')
i = (1234567890)

char = input("enter any char :")

if char == U_C:
    print("char is upper case")
elif char == L_C:
    print("char is lwer case")
elif char == i:
    print("char is integer")
else:
    print("special char")