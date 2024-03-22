n, m = [int(e) for e in input().split()]
mat = [[int(e) for e in input().split()] for i in range(n)]
dic = {}
for i in range(n):
    for j in range(m):
        dic[mat[i][j]] = [i, j]
q = int(input())
for i in range(q):
    x = int(input())
    if x in dic:
        print(*dic[x])
    else:
        print(-1, -1)
