n = input()
a = len(n)
xa, xb, ya, yb = 0,2**a, 0, 2**a
for i in range(a):
    if n[i] == '0':
        xb = (xa + xb) / 2
        yb = (ya + yb) / 2
    elif n[i] == '1':
        xa = (xa + xb) / 2
        yb = (ya + yb) / 2
    elif n[i] == '2':
        xb = (xa + xb) / 2
        ya = (ya + yb) / 2
    else:
        xa = (xa + xb) / 2
        ya = (ya + yb) / 2
print(a, int(xa), int(ya))
