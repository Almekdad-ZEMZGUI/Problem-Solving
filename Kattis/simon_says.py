n = int(input())
for i in range(n):
     c = input()
     cc = c.split(" ")
     if cc[0] == ('Simon') and cc[1] == ('says'):
          cc.remove('Simon')
          cc.remove('says')
          print(' '.join(cc))
