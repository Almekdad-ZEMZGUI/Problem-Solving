n = int(input())
array = [int(ele) for ele in input().split()]
q = int(input())
dic = {}
for ele in array:
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1
 
count_sum_val = {}
for num, count in dic.items():
    if count in count_sum_val:
        count_sum_val[count] += num * count
    else:
        count_sum_val[count] = num * count
 
lis = [0] * (max(count_sum_val) + 1)
for count, sum_val in count_sum_val.items():
    lis[count] = sum_val
accum_lis = [0] * (max(count_sum_val) + 1)
for i in range(1, len(lis)):
    accum_lis[i] = accum_lis[i-1] + lis[i]
 
for i in range(q):
    l, r = [int(e) for e in input().split()]
    len_lis = len(lis)
    if l > len_lis:
        print(0)
    elif r >= len_lis:
        print(accum_lis[-1] - accum_lis[l-1])
    else:
        print(accum_lis[r] - accum_lis[l-1])
