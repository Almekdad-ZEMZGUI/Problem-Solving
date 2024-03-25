n = int(input())
minn = 0
secc = 0
for i in range(n):
    line = [int(e) for e in input().split()]
    minn += line[0]
    secc += line[1]
if (secc / 60 / minn) <= 1:
    print("measurement error")
else:
    print(secc / 60 / minn)
