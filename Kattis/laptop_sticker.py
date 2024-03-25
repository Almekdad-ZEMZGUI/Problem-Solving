line = input().split()
wc, hc, ws, hs = int(line[0]), int(line[1]), int(line[2]), int(line[3])
if wc >= ws + 2 and hc >= hs + 2:
    print("1")
else:
    print("0")
