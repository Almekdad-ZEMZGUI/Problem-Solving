n = int(input())
a = bin(n)[2:]
l = [ele for ele in a]
l.reverse()
st = ''
for elem in l:
     st += str(elem)
print(int(st, 2))
