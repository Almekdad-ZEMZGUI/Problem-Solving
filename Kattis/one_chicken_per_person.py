line = [int(e) for e in input().split()]
n, m = line[0], line[1]
res = m - n
if res  == 1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif res == -1:
    print("Dr. Chaz needs 1 more piece of chicken!")
elif res > 0:
    print("Dr. Chaz will have %d pieces of chicken left over!" % res)
else:
    print("Dr. Chaz needs %d more pieces of chicken!" % abs(res))
