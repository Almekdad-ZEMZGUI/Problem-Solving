n, k = [int(e) for e in input().split()]
arr = [int(e) for e in input().split()]
count = 0
summ = 0
c_summ = []
for i in range(k):
    summ += arr[i]
    c_summ.append(summ)
for i in range(k - 1):
    summ = summ - arr[k - 1 - i] + arr[n - 1 - i]
    c_summ.append(summ)
print(max(c_summ))
