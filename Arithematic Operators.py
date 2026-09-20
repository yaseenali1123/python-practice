#1
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)

#2
import math
r = float(input("Enter radius: "))
area = math.pi * r ** 2
print(f"Area: {area:.2f}")

#3
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print(f"Simple Interest: {si:.2f}")

#4
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c}°C = {f}°F")

f2 = float(input("Enter temperature in Fahrenheit: "))
c2 = (f2 - 32) * 5/9
print(f"{f2}°F = {c2:.2f}°C")

#5
n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3 only")
elif n % 5 == 0:
    print("Divisible by 5 only")
else:
    print("Not divisible by 3 or 5")
