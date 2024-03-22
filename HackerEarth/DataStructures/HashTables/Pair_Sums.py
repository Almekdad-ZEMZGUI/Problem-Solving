n, k = [int(e) for e in input().split()]
arr = [int(e) for e in input().split()]
dic = {}
ex = False
for i in range(n):
    if k - arr[i] in dic:
        print("YES")
        ex = True
        break
    dic[arr[i]] = i
if not ex:
    print("NO")
