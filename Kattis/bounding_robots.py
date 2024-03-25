n = input().split()
while int(n[0]) != 0:
    nn = int(input())
    l = [input() for i in range(nn)]
    a, b = int(n[0]), int(n[1])
    x, y = 0, 0
    xx, yy = 0, 0
    for ele in l:
        if ele[0] == 'r':
            x += int(ele[2:])
            if xx + int(ele[2:]) >= a:
                xx = a-1
            else:
                xx += int(ele[2:])
        elif ele[0] == 'l':
            x -= int(ele[2:])
            if xx - int(ele[2:]) < 0:
                xx = 0
            else:
                xx -= int(ele[2:])
        elif ele[0] == 'u':
            y += int(ele[2:])
            if yy + int(ele[2:]) >= b:
                yy = b-1
            else:
                yy += int(ele[2:])
        else:
            y -= int(ele[2:])
            if yy - int(ele[2:]) < 0:
                yy = 0
            else:
                yy -= int(ele[2:])
    print('Robot thinks', x, y)
    print('Actually at', xx, yy)
    print()
    n = input().split()
