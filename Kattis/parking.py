n = input().split()
t1 = input().split()
t2 = input().split()
t3 = input().split()
tr1 = [e for e in range(int(t1[0]),int(t1[1]))]
tr2 = [e for e in range(int(t2[0]),int(t2[1]))]
tr3 = [e for e in range(int(t3[0]),int(t3[1]))]
mi = int(t1[0])
if mi > int(t2[0]):
     mi = int(t2[0])
     if int(t2[0]) > int(t3[0]):
          mi = int(t3[0])
if mi > int(t3[0]):
     mi =int(t3[0]) 
ma = int(t1[1])
if ma < int(t2[1]):
     ma = int(t2[1])
     if int(t2[1]) < int(t3[1]):
          ma = int(t3[1])
if ma < int(t3[1]):
     ma = int(t3[1])
a ,b ,c = 0, 0, 0
for i in range(mi,ma):
     if i in tr1 and i in tr2 and i in tr3:
          c += 3 * int(n[2])
     elif (i in tr1 and i in tr2 and i not in tr3) or (
          i in tr1 and i in tr3 and i not in tr2) or (
               i in tr2 and i in tr3 and i not in tr1):
          b += 2 * int(n[1])
     elif (i in tr1 and i not in tr2 and i not in tr3) or (
          i in tr3 and i not in tr1 and i not in tr2) or (
               i in tr2 and i not in tr1 and i not in tr3):
          a += int(n[0])
print(a + b + c)
