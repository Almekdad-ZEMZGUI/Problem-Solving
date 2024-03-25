from math import sqrt

n = int(input())
listt = []
for i in range(n):
     st = input()
     stt = int(sqrt(len(st)))
     m = []
     for i in range(0,len(st), stt):
          m.append(st[i:i+stt])
     mm = []
     for i in range(1, len(m)+1):
          for ele in m:
               if i == 1:
                    mm.append(ele[-i:])
               else:
                    mm.append(ele[-i:-i+1])
     listt.append(mm)
for i in range(n):
     st = ''
     for ele in listt[i]:
          st += ele
     print(st)
