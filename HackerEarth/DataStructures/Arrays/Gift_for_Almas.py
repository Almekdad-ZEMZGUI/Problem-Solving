import numpy
n = int(input())
mat = []
for i in range(n):
    line = [int(e) for e in input().split()]
    mat.append(line)
 
d = input()
 
for ele in d:
    if ele =='R':
        mat = numpy.rot90(mat, 3)
    else:
        mat = numpy.rot90(mat)
for a in mat:
    print(*a)
