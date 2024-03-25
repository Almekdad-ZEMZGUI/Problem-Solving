line = input().split()
a, b, c = int(line[0]), int(line[1]), int(line[2])
ab = b - a - 1
bc = c - b - 1
print(max(ab, bc))
