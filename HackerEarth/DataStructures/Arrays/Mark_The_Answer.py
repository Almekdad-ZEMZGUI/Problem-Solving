n, x = [int(e) for e in input().split()]
line = [int(e) for e in input().split()]
 
score = 0
skip = 0
 
for i in range(n):
    if line[i] <= x and skip <= 1:
        score += 1
    elif line[i] > x:
        skip += 1
print(score)
