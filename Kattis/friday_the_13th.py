n = int(input())
for i in range(n):
    s = input().split()
    day, mounth = int(s[0]), int(s[1])
    di = input().split()
    ind = 0
    sh = 0
    j = 1
    res = 0
    for i in range(day):
        if j == 13 and ind == 5:
            res += 1
        if ind == 6:
            ind = 0
        else:
            ind += 1

        if j == int(di[sh]):
            sh += 1
            j = 1
        else:
            j += 1
    print(res)
