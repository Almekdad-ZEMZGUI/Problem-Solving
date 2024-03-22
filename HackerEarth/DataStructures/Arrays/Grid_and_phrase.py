n, m = [int(e) for e in input().split()]
 
mat = []
for i in range(n):
    line = [e for e in input()]
    mat.append(line)
count = 0
 
for i in range(n):
    for j in range(m):
        if mat[i][j] == "s":
            if j + 3 < m and mat[i][j+1] == "a" and mat[i][j+2] == "b" and mat[i][j+3] == "a":
                count += 1
            if i + 3 < n and mat[i+1][j] == "a" and mat[i+2][j] == "b" and mat[i+3][j] == "a":
                count += 1
            if j + 3 < m and i + 3 < n and mat[i+1][j+1] == "a" and mat[i+2][j+2] == "b" and mat[i+3][j+3] == "a":
                count += 1
            if j + 3 < m and i - 3 >= 0 and mat[i-1][j+1] == "a" and mat[i-2][j+2] == "b" and mat[i-3][j+3] == "a":
                count += 1
 
print(count)
