n = input().split()
l = [1, 1, 2, 2, 2, 8]
out = []
for i in range(6):
    a = int(l[i]) - int(n[i])
     out.append(a)
for ele in out:
    print(ele, end=' ')

