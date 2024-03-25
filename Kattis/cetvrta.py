l1 = input().split()
l2 = input().split()
l3 = input().split()
if l1[0] == l2[0]:
     a = l3[0]
elif l1[0] == l3[0]:
     a = l2[0]
else:
     a = l1[0]
if l1[1] == l2[1]:
     b = l3[1]
elif l1[1] == l3[1]:
     b = l2[1]
else:
     b = l1[1]
print(a, b)
