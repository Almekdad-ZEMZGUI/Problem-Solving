n = int(input())
arr = [int(e) for e in input().split()]
 
count = 1
for i in range(n - 1):
    if arr[i] > arr[i+1]:
        count += 1
print(count)
