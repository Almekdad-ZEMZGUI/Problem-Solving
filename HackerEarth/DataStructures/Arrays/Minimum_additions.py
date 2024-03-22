t = int(input())
for i in range(t):
    n, k = [int(e) for e in input().split()]
    array = [int(e) for e in input().split()]
    sum_array = sum(array)
    size_array = n
    if sum_array / size_array <= k:
        print(0)
        continue
    else:
        p = (sum_array // (k + 1)) + 1
 
    print(max(0, p - n))
