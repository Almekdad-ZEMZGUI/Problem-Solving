import sys

for v in sys.stdin:
    v2 = v.split()
    x = int(v2[0]) - int(v2[1])
    print(abs(x))
