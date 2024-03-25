n = input().split()
a = 0
b = 0
if int(n[1]) >= 45:
     a = int(n[0])
     b = (int(n[1]) - 45)
elif int(n[0]) == 0:
     a = int(n[0]) + 23
     b = abs(int(n[1]) + 60 - 45)
else:
     a = int(n[0]) - 1
     b = abs(int(n[1]) + 60 - 45)
print(a, b)
