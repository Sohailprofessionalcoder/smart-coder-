#1.even/odd
num = int(input("enter num - "))
if num & 1 == 0:
    print("even")
else :
    print("odd")

#2.swap
a = 2
b = 3 
a = a^b
b = a^b
a = a^b

print(a,b)

#3.shift operators
n = int(input("enter n :"))
n <<1 , n>>1
print(n)


#4.set 
k = int(input("enter k = "))

if n (1<<k) != 0 :
    print("set")
else:
    print("not set")
    
#5.count bits
while n >0:
    n = n & (n-1)
    n += 1
    
print(n)