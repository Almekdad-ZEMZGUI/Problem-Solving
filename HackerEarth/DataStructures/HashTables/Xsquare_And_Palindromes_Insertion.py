t = int(input())
for i in range(t):
    s = input().strip()
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    odd = 0
    for v in dic.values():
        if v % 2 == 1:
            odd += 1
    if odd == 1 or odd == 0:
       print(0)
    else:
       print(odd - 1)
