t = int(input())
for i in range(t):
    line = [int(e) for e in input()]
    line.reverse()
    trans = [line[0]]
    count = 0
    for i in range(1,len(line)):
        if i % 2 == 1:
            trans.append(line[i] * 2)
        else:
            trans.append(line[i])
    for ele in trans:
        if ele // 10 > 0:
            count += ele // 10
            count += ele % 10
        else:
            count += ele
    if int(count / 10) == count / 10:
        print("PASS")
    else:
        print("FAIL")
