l=[]
for i in range(5):
     a = 0
     n = input().split()
     for i in range(4):
          a += int(n[i])
     l.append(a)
b = max(l)
index = 0
for i in range(len(l)):
     if l[i] == b:
          index = i + 1
print(index, b)
