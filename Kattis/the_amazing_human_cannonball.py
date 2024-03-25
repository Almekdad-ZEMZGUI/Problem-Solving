import math

n = int(input())
for i in range(n):
     line = input().split()
     t = float(line[2]) / (float(line[0]) * math.cos(math.radians(float(line[1]))))
     y = float(line[0]) * t * math.sin(math.radians(float(line[1]))) - (0.5*9.81*(t**2))
     if float(line[3]) < y+1 < float(line[4]) and float(line[3]) < y-1 < float(line[4]):
          print('Safe')
     else:
          print('Not Safe')
