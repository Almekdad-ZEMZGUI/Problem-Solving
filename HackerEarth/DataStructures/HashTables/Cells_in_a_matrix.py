n, k = [int(e) for e in input().split()]
row = [int(e) for e in range(1, n+1)]
col = [int(e) for e in range(1, n+1)]
 
for _ in range(k):
    a, b = [int(e) for e in input().split()]
 
    if a in row:
        row.remove(a)
    if b in col:
        col.remove(b)
    print(len(row)*len(col), end=" ")
