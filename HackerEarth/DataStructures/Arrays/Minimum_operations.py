n = int(input())
array = [int(e) for e in input().split()]
count = 1
for i in range(1, n):
    if array[i] != array[i-1]:
        count += 1
print(count)
