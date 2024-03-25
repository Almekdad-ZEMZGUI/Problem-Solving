n = int(input())
for i in range(n):
     fir = input()
     sec = input()
     out = ''
     for i in range(len(fir)):
          if fir[i] == sec[i]:
               out += '.'
          else:
               out += '*'
     print(fir)
     print(sec)
     print(out)
     print('\n')
