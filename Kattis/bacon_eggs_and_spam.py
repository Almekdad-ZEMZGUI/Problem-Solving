while True:
    n = int(input())
    d = {}
    if n == 0:
        break
    for i in range(n):
        s = input().split()
        for ele in s[1:]:
            if ele in d:
                d[ele].append(s[0])
            else:
                d[ele] = [s[0]]
    keys = []
    for k, v in d.items():
        keys.append(k)
    keys = sorted(keys)
    for ele in keys:
        if ele in d:
            a = sorted(d[ele])
            st = ''
            for el in a:
                st += el + ' ' 
            print(ele + ' ' + st)
    print()
