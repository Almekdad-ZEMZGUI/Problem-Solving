t = int(input())
for _ in range(t):
    n = int(input())
    mat = []
    for _ in range(n):
        line = [int(e) for e in input()]
        mat.append(line)
    # symmetric rows
    res = True
    for i in range(n):
        s = 0
        e = -1
        for j in range(n // 2):
            if mat[i][s] != mat[i][e]:
                res = False
                break
            s += 1
            e -= 1
        if not res:
            break
    # symmetric cols
    res2 = True
    for j in range(n):
        s = 0
        e = -1
        for i in range(n // 2):
            if mat[s][j] != mat[e][j]:
                res2 = False
                break
            s += 1
            e -= 1
        if not res:
            break
    if res and res2:
        print('YES')
    else:
        print('NO')
