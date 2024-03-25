from math import sqrt

a = input()
b = a.split()
for i in range(int(b[0])):
     c = int(input())
     demention = sqrt((int(b[1]))**2 + (int(b[2]))**2)
     if c <= demention:
          print('DA')
     else :
          print('NE')
