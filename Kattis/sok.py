n = input().split()
nn = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])
x, y, z = int(nn[0]), int(nn[1]), int(nn[2])
l = [a / x, b / y, c / z]
u, uu, uuu = min(l) * x, min(l) * y, min(l) * z
print(a - u, b - uu, c - uuu)
