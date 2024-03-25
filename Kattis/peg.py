line = [input() for i in range(7)]
res = 0
for i in range(7):
    for j in range(7):
        if line[i][j] == ".":
            if j+2 < 7 and line[i][j+1] == line[i][j+2] == "o":
                res += 1
            if j-2 >= 0 and line[i][j - 1] == line[i][j - 2] == "o":
                res += 1
            if i+2 < 7 and line[i+1][j] == line[i+2][j] == "o":
                res += 1
            if i-2 >= 0 and line[i-1][j] == line[i-2][j] == "o":
                res += 1

print(res)
