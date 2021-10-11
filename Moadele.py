import math

a = int(input("Inset a please:"))
b = int(input("Insert b please:"))
c = int(input("Insert c please:"))

adad = (b**2) - (4*a*c)
#delta = adad**0.5
delta = math.sqrt(adad)

x1 = (-b + delta)/2*a
x2 = (-b - delta)/2*a

if x1 == x2:
    print("Rishe Mosaaf, you have two same answeres that are equal to:", x1)
    exit()

print("Answers are:", x1,x2)
