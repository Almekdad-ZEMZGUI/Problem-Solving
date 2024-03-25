n = int(input())
for i in range(n):
    line = input().split()
    for i in range(1, int(line[0]) - 1):
        if int(line[i]) + 1 != int(line[i+1]) and line[i+1] != line[-1]:
            print(i + 1)
            break
