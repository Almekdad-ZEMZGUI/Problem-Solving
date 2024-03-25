n = int(input())
res = 0
for i in range(n):
    k = input()
    if 'CD' not in k:
        res += 1
print(res)
