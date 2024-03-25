n = int(input())
for i in range (n):
     m = input()
     p = m.split(' ')
     if int(p[0])+int(p[1]) == int(p[2]) or int(p[0]) - int(p[1]) == int(p[2]) or int(p[1]) - int(p[0]) == int(p[2]) or int(p[0]) * int(p[1]) == int(p[2]) or int(p[0]) / int(p[1]) == int(p[2]) or int(p[1]) / int(p[0]) == int(p[2]):
          print('Possible')
     else:
          print('Impossible')
