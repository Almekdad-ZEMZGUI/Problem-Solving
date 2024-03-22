t = int(input())
for _ in range(t):
    n = int(input())
    dic = dict()
    for i in range(n):
        x = input().split()
        if x[0] in dic:
            dic[x[0]].append(int(x[1]))
        else:
            dic[x[0]] = [int(x[1])]
    dic2 = {}
    for k, v in dic.items():
        v.sort()
        if len(v) <= 3:
            sm = sum(v)
            dic2[k] = sm
        else:
            sm = sum(v[-3:])
            dic2[k] = sm
    res = []
    maxi = max(dic2.values())
    for k, v in dic2.items():
        if v == maxi:
            res.append(k)
    if len(res) == 1:
        print(res[0], maxi)
    else:
        res = sorted(res)
        print(res[0], maxi)
