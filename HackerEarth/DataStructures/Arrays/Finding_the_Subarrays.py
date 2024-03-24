n = int(input())
arr = [int(e) for e in input().split()]
cum_sum = [0] * (n + 1)
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + arr[i]
res = []
x = 0
len_remain = n
for i in range(n):
    for j in range(i, n):
        len_remain -= 1
        sum_sub = cum_sum[j+1] - cum_sum[i]
        avg_sub = sum_sub/(j-i+1)
        if len_remain != 0:
            remain_avg = (cum_sum[n] - sum_sub) / len_remain
        else:
            remain_avg = 0
        if avg_sub > remain_avg:
            res.append((i+1, j+1))
            x += 1
    len_remain = n
print(x)
res.sort()
for ele in res:
    print(*ele)

