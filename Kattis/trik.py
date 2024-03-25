a = input()
b = 1
for element in a:
     if element =='A' and b == 1:
          b += 1
     elif element == 'A' and b == 2:
          b = 1
     elif element == 'B' and b == 2:
          b += 1
     elif element == 'B' and b == 3:
          b = b - 1
     elif element == 'C' and b == 3:
          b = 1
     elif element == 'C' and b == 1:
          b += 2
print(b)
