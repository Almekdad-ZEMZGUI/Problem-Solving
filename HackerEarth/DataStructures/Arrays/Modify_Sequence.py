n = int(input())
arr = [int(e) for e in input().split()]
a= False
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        arr[i+1] = arr[i+1] - arr[i]
        arr[i] = 0
    else:
        a = True
        print('NO')
        break
if not a:
    if sum(arr) == 0:
        print('YES')
    else:
        print('NO')
