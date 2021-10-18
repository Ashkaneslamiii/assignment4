a = int(input())
b = int(input())

for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
        bmm = i

print(bmm)

kmm = a
for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            if i <= kmm and i !=1 :
                kmm = i 

print(kmm)