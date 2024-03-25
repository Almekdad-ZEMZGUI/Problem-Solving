n = input().split()
a = int(n[0])
b = int(n[1])
mx = 0
out = 0
for i in range(b):
     s = input().split()
     if s[0] == 'enter':
          mx += int(s[1])
          if mx > a:
               out += 1
               mx -= int(s[1])
     else:
          mx -= int(s[1])
print(out)
