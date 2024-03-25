s = input()
a, b, c, d = 0, 0, 0, 0
for ele in s:
     if ele == '_':
          a += 1
     elif ord('a') <= ord(ele) <= ord('z'):
          b += 1
     elif ord('A') <= ord(ele) <= ord('Z'):
          c += 1
     else:
          d += 1
print(a / int(len(s)))
print(b / int(len(s)))
print(c / int(len(s)))
print(d / int(len(s)))
