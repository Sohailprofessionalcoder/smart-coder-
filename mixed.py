#1.check the char
ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

#2.cp/sp
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print(f"Profit: {sp - cp:.2f}")
elif cp > sp:
    print(f"Loss: {cp - sp:.2f}")
else:
    print("No profit, no loss")

#3. co-ordinates
x = float(input("Enter x: "))
y = float(input("Enter y: "))
if x == 0 and y == 0:
    print("Point is at the origin")
elif x == 0:
    print("Point is on the Y-axis")
elif y == 0:
    print("Point is on the X-axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else:
    print("Quadrant IV")

#4.armstrong number
n = int(input("Enter a 3-digit number: "))
s = str(n)
total = sum(int(d) ** 3 for d in s)
if total == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

#5.time complexity
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
if hours > 40:
    salary = 40 * rate + (hours - 40) * rate * 1.5
else:
    salary = hours * rate
print(f"Salary: {salary:.2f}")

#6.small atm
balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))
MIN_BALANCE = 500

if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
elif balance - amount < MIN_BALANCE:
    print("Transaction declined: insufficient balance (minimum balance rule)")
else:
    balance -= amount
    print(f"Withdrawal successful. New balance: {balance:.2f}")


#7. clock angle
hour = int(input("Enter hour (0-12): "))
minute = int(input("Enter minute (0-59): "))

hour = hour % 12
hour_angle = 0.5 * (hour * 60 + minute)
minute_angle = 6 * minute
angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)
print(f"Angle between hands: {angle:.2f} degrees")