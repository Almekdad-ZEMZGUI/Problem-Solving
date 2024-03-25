while True:
    n = input().split()
    n1, n2 = int(n[0]), int(n[1])
    if n1 == 0 and n2 == 0:
        break
    else:
        if n1 + n2 == 13:
            print('Never speak again.')
        else:
            if n1 > n2:
                print('To the convention.')
            elif n1 < n2:
                print('Left beehind.')
            elif n1 == n2:
                print('Undecided.') 
