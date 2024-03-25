n = input().split()
nn = input().split()
l = [0, int(n[0])]
for ele in nn:
    l.append(int(ele))
l.sort()
l.reverse()
m = []
for i in range(len(l) - 1):
    for j in range(len(l) - 1):
        if l[i] - l[j+1] > 0:
            m.append(l[i] - l[j+1])
m.sort()
m = list(set(m))
for ele in m:
    if ele == m[-1]:
        print(ele)
    else:
        print(ele, end=' ')
