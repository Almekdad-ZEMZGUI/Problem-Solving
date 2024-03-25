n = int(input())
for i in range(n):
     l1 = []
     x1 = 0
     cases1 = int(input())
     for p in range(cases1):
          cities1 = input()
          l1.append(cities1)
     l1 = set(l1)
     for element in (l1):
          x1 = x1+1
     print(x1)
