import math
n = int(input())
arr = [int(e) for e in input().split()]
count = 0
cum_sum = [0] * n
cum_sum[0] = arr[0]
for x in range(1, n):
    cum_sum[x] = cum_sum[x-1] + arr[x]
for i in range(n):
    for j in range(i, n):
        sum_sub = cum_sum[j] - cum_sum[i-1] if i != 0 else cum_sum[j]
        if math.sqrt(sum_sub).is_integer():
            count += 1
print(count)
