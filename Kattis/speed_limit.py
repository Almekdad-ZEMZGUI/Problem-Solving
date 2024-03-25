while True:
    n = int(input())
    if n == -1:
        break
    ss = []
    tt = []
    for i in range(n):
        line = input().split()
        ss.append(line[0])
        tt.append(line[1])
    out = 0
    a = 0
    for i in range(len(ss)):
        out += int(ss[i]) * (int(tt[i]) - a)
        a = int(tt[i])
    print("%d miles" % out)
