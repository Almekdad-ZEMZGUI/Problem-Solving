n = int(input())
arr = [int(e) for e in input().split()]
count = 0
freq = {}
for i in range(n):
    cond = (i + 1)**2 + arr[i]
    if cond in freq:
        freq[cond] += 1
    else:
        freq[cond] = 1
for i in range(n):
    complter = arr[i] - (i + 1)**2
    if complter in freq:
        count += freq[complter]
print(count)
