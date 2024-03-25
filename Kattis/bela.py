n = input().split()
sm = 0
for i in range(int(n[0])*4):
     a = input()
     if a[0] == 'A':
          sm += 11
     elif a[0] == 'K':
          sm += 4
     elif a[0] == 'Q':
          sm += 3
     elif a[0] == '8' or a[0] == '7':
          sm += 0
     elif a[0] == 'T':
          sm += 10
     elif a[0] == 'J':
          if a[1] == n[1]:
               sm += 20
          else:
               sm += 2
     elif a[0] == '9':
          if a[1] == n[1]:
               sm += 14
          else:
               sm += 0
print(sm)
