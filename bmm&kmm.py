a = int(input())
b = int(input())

for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
        bmm = i





if a > b:
    tmp = b 
    b = a
    a = tmp 
print(a,b)
for i in range(b,(a*b)+1):
    if i%a == 0 and i%b == 0:
        kmm = i
        break


print(bmm)
print(kmm)
