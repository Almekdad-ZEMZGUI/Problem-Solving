line = input().split()
arr = input().split()
n = int(line[0])
step = int(line[1])
for i in range(step-1, n, step):
    print(arr[i], end=" ")
