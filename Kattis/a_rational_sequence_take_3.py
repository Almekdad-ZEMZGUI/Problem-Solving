n = int(input())
for i in range (n):
     a, b = 1, 1
     num = input().split()
     num1 = int(num[1])
     st = ''
     st2 = ''
     while num1 != 1:
          if num1 % 2 == 0:
               num1 /= 2
               st += 'L'
          else:
               num1 = (num1 - 1) / 2
               st += 'R'
     for j in range(len(st)):
          ind = len(st) - 1 - j
          st2 += st[ind]
     if len(st2) == 0:
          print(num[0], '1/1')
     else:
          for ele in st2:
               if ele == 'L':
                    b = a + b
               else:
                    a = a + b
          print('{} {}/{}'.format(num[0], a, b))
