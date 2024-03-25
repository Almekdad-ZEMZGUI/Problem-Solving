n = [int(e) for e in input().split()]
l = [(d1 + d2 + 2) for d1 in range(n[0]) for d2 in range(n[1])]
dict = {}
for ele in l:
     if ele in dict:
          dict[ele] += 1
     else:
          dict[ele] = 1
_max = max(dict.values())
[print(k) for k, v in dict.items() if v == _max]
