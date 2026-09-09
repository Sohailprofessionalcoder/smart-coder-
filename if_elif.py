#1.odd/even 
n = int(input("enter value of n : "))
if n%2==0:
    print("even")
else:
    print("odd")

#2.leap year
year = int(input("enter year :"))
if year % 400 == 0:
    print("leap year")
else :
    print("non leap year ")

#3.largest of two num
a = int(input("enter a :"))
b = int(input("enter b :"))
if a<b:
    print("a is largest ")
elif b<a:
    print("b is largest ")
else:
    print("two are equal")

#4.largest of three numbers
c = int(input("enter c :"))

if a<b and a<c:
    print("a is largest")
elif b<a and b<c:
    print("b is largest")
else :
    print("c is largest")

#5.vowel and consent
s = int(input("enter a single char"))

vowel = {'a','e','i','o','u','A','E','I','O','U'}

if s == vowel:
    print("vowels")
else:
    print("consonents")


#6.ticket 
age = int(input("enter age : "))
if age<5:
    print("ticket price = 5Rs ")
elif age > 5 and age<20 :
    print("ticket price = 10Rs")
else :
    print("ticekt price = 15Rs")

#7time reading
time = int(input("enter time :"))

if 5< time > 12:
    print("morning")
elif 12< time > 16 :
    print("afternoon")
elif 17 < time > 20 :
    print("evening")
else:
    print("night") 