n = int(input())
line = [int(e) for e in input().split()]
count = 0
for e in line:
    if e < 0:
        count += 1
print(count)
