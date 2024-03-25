import sys

a = 1
for i in sys.stdin:
    res = 0
    s = i.split()
    er, ma = int(s[0]), int(s[1])
    if er == 0 and ma == 0:
        res = 0
    else:
        while True:
            if er % 365 == 0 and ma % 687 == 0:
                break
            rest = er % 365
            to_add = 365 - rest
            er += to_add
            ma += to_add
            res += to_add
    print('case {}: {}'.format(a, res))
    a += 1
