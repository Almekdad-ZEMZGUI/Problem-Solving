n = int(input())
a = 1
b = 0
for i in range(n):
     to_b = a
     a = 0
     to_a = b

     a += to_a
     b += to_b
print(a, b)
