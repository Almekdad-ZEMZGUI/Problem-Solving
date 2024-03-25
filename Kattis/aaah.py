a = input()
b = input()
l1 = []
l2 = []
for letters in a:
     l1.append(letters)
for letters2 in b:
     l2.append(letters2)
if len(l1) >= len(l2):
     print('go')
else:
     print('no')
