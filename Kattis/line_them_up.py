n = int(input())
nms = []
for i in range(n):
    nms.append(input())
nms1 = sorted(nms)
nms_rev = []
for i in reversed(nms1):
    nms_rev.append(i)
if nms1 == nms:
    print('INCREASING')
elif nms == nms_rev:
    print('DECREASING')
else:
    print('NEITHER')
