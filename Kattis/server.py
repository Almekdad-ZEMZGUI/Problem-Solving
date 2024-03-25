n = input().split()
nn = input().split()
l = []
for ele in nn:
    l.append(int(ele))
a = 0
res = 0
if int(n[1]) < int(nn[0]):
    res = 0
elif int(n[1]) >= sum(l):
    res = int(n[0])
else:
    for i in range(int(n[0])):
        a += int(nn[i])
        if a > int(n[1]):
            res = i
            break
print(res)
