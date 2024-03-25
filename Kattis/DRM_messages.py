n = input()
a = n[:int(len(n)/2)]
b = n[int(len(n)/2):]
sm = 0
sm1 = 0
def f(x):
     for i in a:
          for k, v in d.items():
               if x == v:
                    return(k)
d = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,
     'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,
     'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,
     'W':22,'X':23,'Y':24,'Z':25}
ai = ''
bi = ''
for i in a:
          sm += d[i]
for i in b:
          sm1 += d[i]
for i in a:
     r = int(d[i]) + sm
     t = r % 26
     ai += f(t)
for i in b:
     y = int(d[i]) + sm1
     t = y % 26
     bi += f(t)
res = ''
for i in range(len(ai)):
     e = d[bi[i]] + d[ai[i]]
     w = e % 26
     res += f(w)
print(res)
