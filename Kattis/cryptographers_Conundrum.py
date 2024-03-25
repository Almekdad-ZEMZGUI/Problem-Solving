s = input()
out = 0
for i in range(0, len(s), 3):
          a = s[i:i+3]
          if a[0] != 'P':
               out += 1
          if a[1] != 'E':
               out += 1
          if a[2] != 'R':
               out += 1
print(out)
