l = []
line = input().split()
while 1:
     if line == ['-1']:
          break
     l.append(line)
     line = input().split()
s = 0
for i in l:
     if i[2] == 'right':
          s += int(i[0])
a = []
b = []
for i in l:
     if i[2] == 'wrong':
          a.append(i[1:2])
for i in l:
     if i[2] == 'right':
          b.append(i[1:2])
res = 0
for ele in b:
     if ele in a:
          c = a.count(ele)
          res += c
e = 0
for ele in l:
     if ele[2] == 'right':
          e+=1
print(e, s + res * 20)
