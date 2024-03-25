n = int(input())
a = 1
while n != 0:
    l = []
    for i in range(n):
        line = input()
        l.append(line)
    m = [0] * len(l)
    left, ind_l, ind_r = True, 0, len(l) - 1
    for i in range(len(l)):
        if left:
            m[ind_l] = l[i]
            ind_l += 1
            left = False
        else:
            m[ind_r] = l[i]
            ind_r -= 1
            left = True
    print("SET", a)
    for e in m:
        print(e)
    a += 1
    n = int(input())
