l = []
for i in range(10):
     a = int(input())
     b = a % 42
     l.append(b)
l = set(l)
print(len(l))
