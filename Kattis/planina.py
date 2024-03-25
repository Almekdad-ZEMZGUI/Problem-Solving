n = int(input())
a = 3
b = 1
for i in range(n):
     b = a**2
     a = a + a - 1
print(b)
