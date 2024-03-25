n = int(input())
res = 0
for i in range(n):
     nn = input()
     a = nn[:-1]
     b = nn[-1:]
     res += int(a) ** int(b)
print(res)
