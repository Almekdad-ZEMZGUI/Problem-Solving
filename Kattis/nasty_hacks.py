n = int(input())
for i in range(n):
     line = input().split()
     if int(line[1]) - int(line[2]) == int(line[0]):
          print('does not matter')
     elif int(line[1]) - int(line[2]) > int(line[0]):
          print('advertise')
     else:
          print('do not advertise')
