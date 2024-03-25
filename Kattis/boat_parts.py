n = input().split()
a, b = int(n[0]), int(n[1])
l = []
out = 0
for i in range(b):
     l.append(input())
     if len(set(l)) == a:
          out = i + 1
          break
if len(set(l)) < a:
     print('paradox avoided')
else:
     print(out)
