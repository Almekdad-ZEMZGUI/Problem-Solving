import sys

c = 1
for line in sys.stdin:
    arr = [int(e) for e in line.split()]
    print("Case {}: {} {} {}".format(c, min(arr[1:]), max(arr[1:]), max(arr[1:]) - min(arr[1:])))
    c += 1
