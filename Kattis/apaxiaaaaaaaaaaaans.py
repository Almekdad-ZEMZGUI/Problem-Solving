a = input()
l = [element for element in a]
l1 = []
pr = ''
for i in range(len(l)):
     if l[i] != pr:
          l1.append(l[i])
          pr = l[i]
for ele in l1:
     print(ele, end='')
