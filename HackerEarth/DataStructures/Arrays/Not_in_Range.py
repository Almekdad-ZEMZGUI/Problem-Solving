import sys

n = int(input())
ranges = []
if n == 0:
    print(sum(x for x in range(1000001)))
    sys.exit(0)
for _ in range(n):
    l, r = [int(num) for num in input().split()]
    ranges.append((l, r))
ranges.sort()
merge_r = []
start, end = ranges[0]
for i in range(1, n):
    l, r = ranges[i]
    if l <= end:
        end = max(end, r)
    else:
        merge_r.append((start, end))
        start, end = l, r
merge_r.append((start, end))
res = sum(x for x in range(1, merge_r[0][0]))
for i in range(len(merge_r) - 1):
    res += sum(x for x in range(merge_r[i][1] + 1, merge_r[i+1][0]))
res += sum(x for x in range(merge_r[-1][1] + 1, 1000001))

print(res)

