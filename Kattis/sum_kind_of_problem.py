n = int(input())
for i in range(n):
    line = input().split()
    n1 ,n2 = line[0] ,int(line[1])
    print(n1, int(n2 * (n2+1) / 2), int(n2**2), int(n2 * (n2 + 1)))

