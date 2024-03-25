line = input()
l = []

while line != "0 0":
    l.append(line)
    line = input()

for line in l:
    a, b = line.split()
    a, b = int(a), int(b)
    div = a // b
    r = a % b
    print(div, r, "/", b)
