n = input()
l = [int(element) for element in n]
def f(x, y):
     if set(x).difference(set(y)) != set() or len(x) != len(y):
          return False
     else:
          a = set(x)
          var = True
          for element in a:
               occ_x = len([i for i in x if i == element])
               occ_y = len([i for i in y if i == element])
               if occ_x != occ_y:
                    var = False
          return var
     
res = 0
for i in range(int(n) + 1, 1000000):
     si = str(i)
     l1 = [int(ele) for ele in si]
     if f(l,l1):
          res = i
          break
print(res)
