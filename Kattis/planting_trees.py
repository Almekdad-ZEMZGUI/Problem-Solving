n = int(input())
t = input().split()
t = [int(ele)for ele in t]
tt = sorted(t)
tt.reverse()
l = []
i = 1
for j in range(len(tt)):
     l.append(int(tt[j]) + i)
     i += 1
print(max(l) + 1)
