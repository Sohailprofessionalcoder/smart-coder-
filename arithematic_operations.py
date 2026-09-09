"""1.arithamatic operations"""

a = int(input("enter a : "))
b = int(input("enter b : "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#2.area of circle
r = int(input("enter radius : "))
area = 3.14*r*r
print(area)


#3.simple intrest 
P = int(input("enter principle amoumt : "))
R = int(input("enter rate of intrest : "))
T = int(input("enter time years : "))

S = (P+R+T)/100
print(S)

#4.Celcius to farenhiet 
c = int(input("enter celcius : "))

f = (C*9/5)+32
print("farenhiet = ",f)

#5.divisible check
n = int(input("enter a num to check divisible : "))

if n % 3 == 0 :
    print("divisible with 3")
elif n % 5 == 0 :
    print("divisible by 5 ")