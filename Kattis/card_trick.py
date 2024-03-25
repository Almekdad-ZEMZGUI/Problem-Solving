n = int(input())
for i in range(n):
    m = int(input())
    l = [0] * m
    ind = 0
    put = 1
    jump = 1
    while 0 in l:
        if put == m:
            ind_0 = l.index(0)
            l[ind_0] = m
            break
        res = 0
        while res != jump:
            if l[ind] == 0:
                res += 1
            ind = (ind + 1) % m
        while l[ind] != 0:
            ind = (ind + 1) % m
        l[ind] = put
        put += 1
        jump += 1
    for e in range(len(l)):
        if e != m - 1:
            print(l[e], end=" ")
        else:
            print(f"{l[e]}")
