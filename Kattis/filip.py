a = input()
aa = a.split()
A = int(aa[0][::-1])
B = int(aa[1][::-1])
if A > B:
     print(A)
else:
     print(B)
