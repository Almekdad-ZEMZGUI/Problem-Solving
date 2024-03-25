rc = input().split()
r, c = int(rc[0]), int(rc[1])
matrix = []
for i in range(r):
     matrix.append(input())
f, s, t, e, m = 0, 0, 0, 0, 0
for i in range(r-1):
     for j in range(c-1):
          a = matrix[i][j]
          b = matrix[i][j+1]
          x = matrix[i+1][j]
          y = matrix[i+1][j+1]
          if a == "#" or b == "#" or x == "#" or y == "#":
               continue
          elif a == b == x == y == '.':
               f += 1
          else:
               num_x = [a, b, x, y].count("X")
               if num_x == 1:
                    s += 1
               elif num_x == 2:
                    t += 1
               elif num_x == 3:
                    e += 1
               else:
                    m += 1
print(f)
print(s)
print(t)
print(e)
print(m)
