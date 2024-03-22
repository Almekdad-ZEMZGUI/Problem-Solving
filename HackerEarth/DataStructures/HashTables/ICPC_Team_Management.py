t = int(input())
for _ in range(t):
    n, k = [int(e) for e in input().split()]
    dic = {}
    for i in range(n):
        s = input()
        ln = len(s)
        if ln in dic:
            dic[ln].append(s)
        else:
            dic[ln] = [s]
    for v in dic.values():
        if len(v) % k != 0 and k != 1:
            print('Not possible')
            break
    else:
        print('Possible')
