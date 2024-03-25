L = int(input())
D = int(input())
X = int(input())
l = [i for i in range(L, D+1)]
m = []
for i in range(L, D+1):
     st = str(i)
     sm = 0
     for ele in st:
          sm += int(ele)
     if sm == X:
          m.append(i)
print(m[0])
print(m[-1])
