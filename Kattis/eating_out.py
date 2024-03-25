line = [int(e) for e in input().split()]
m, a, b, c = line[0], line[1], line[2], line[3]
if a + b + c <= 2 * m:
    print("possible")
else:
    print("impossible")
