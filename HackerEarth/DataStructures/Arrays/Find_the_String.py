t = int(input())
for _ in range(t):
    n, m = [int(e) for e in input().split()]
    mat = []
    for i in range(n):
        line = [e for e in input()]
        mat.append(line)
    s = input()
    res = True
    a = 0
    for i in range(len(s)):
        if i % len(mat) == 0 and i != 0:
            a = 0
        if s[i] not in mat[a]:
            res = False
            break
        mat[a].remove(s[i])
        a += 1
    if res:
        print("Yes")
    else:
        print("No")
