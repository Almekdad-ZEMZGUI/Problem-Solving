from math import pi

l = input().split()
while(float(l[0]) != 0):
      air = (float(l[0])**2) * pi
      res = ((2*float(l[0]))**2) * int(l[2]) / int(l[1])
      print(air, res)
      l = input().split()
