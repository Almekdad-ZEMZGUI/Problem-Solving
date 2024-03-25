n = int(input())
for i in range(n):
     a = int(input())
     res = 1
     for j in range(1, a+1):
          res *= j
     print(res % 10)

