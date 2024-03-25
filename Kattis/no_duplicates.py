a = input()
b = a.split(" ")
n = 0
m = 0
for element in b:
     n = n + 1
for element in set(b):
     m = m + 1

if m == n:
     print("yes")
else:
     print("no")
