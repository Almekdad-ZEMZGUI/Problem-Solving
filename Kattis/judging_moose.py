n = input().split()
a = int(n[0])
b = int(n[1])
if a == b and a != 0:
     print('Even', a + b)
elif a != b:
     if a > b:
          b = a
          print('Odd', a + b)
     else:
          a = b
          print('Odd', a + b)
else:
     print('Not a moose')
