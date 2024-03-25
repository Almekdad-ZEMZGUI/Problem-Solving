pot = []
k = input()
while True:
     line = input()
     if line == '-1':
          break
     pot.append(line.split())
m = [k]
while True:
     a = False
     for element in pot:
          if k in element[1:]:
               k = element[0]
               m.append(k)
               a = True
               break
     if a == False:
          break
for ele in m:
     print(ele, end=' ')
