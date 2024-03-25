from math import pi

n = input().split()
n1, n2 = int(n[0]), int(n[1])
print((((n2 - n1)**2 * pi) * 100) / (n1**2 * pi))
