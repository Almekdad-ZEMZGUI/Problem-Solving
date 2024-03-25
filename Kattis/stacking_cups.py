import collections

n = int(input())
d = {}
for i in range(n):
     s = input().split()
     if 'a' <= s[0] <= 'z':
          d[int(s[1])] = s[0]
     else:
          s.reverse()
          d[int(int(s[1])/2)] = s[0]
od = collections.OrderedDict(sorted(d.items()))
for k, v in od.items():
     print(v)
