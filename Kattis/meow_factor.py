n = int(input())
print([i for i in range(128, 0, -1) if not n % (i**9)][0])
