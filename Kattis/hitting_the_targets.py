from math import sqrt

n = int(input())
l = []
m = []
for i in range(n):
    l.append(input().split())
nn = int(input())
for i in range(nn):
    m.append(input().split())
for ele in m:
    res = 0
    x, y = int(ele[0]), int(ele[1])
    for el in l:
        if el[0]=='rectangle':
            if int(el[1]) <= x <= int(el[3]) and int(el[2]) <= y <= int(el[4]):
                res += 1
        else:
            dis = sqrt(((int(el[1]) - x)**2) + ((int(el[2])-y)**2))
            if dis <= int(el[3]):
                res += 1
    print(res)
