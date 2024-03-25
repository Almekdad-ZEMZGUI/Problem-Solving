import sys

l = []
for i in sys.stdin:
    l.extend([e for e in i.split()])
res = sorted(set([e + f for e in l for f in l if e != f]))
for ele in res:
    print(ele)
