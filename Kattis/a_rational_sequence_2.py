n = int(input())
for i in range(n):
    n1 = input().split()
    num = n1[1]
    num = num.split('/')
    x, y = int(num[0]), int(num[1])
    st = []
    res = 1
    while x != 1 or y != 1:
        if x < y:
            st.append('L')
            y -= x
        else:
            st.append('R')
            x -= y
    st.reverse()
    if len(st) == 0:
        print(n1[0], '1')
    else:
        for e in st:
            if e == 'L':
                res *= 2
            else:
                res = res * 2 + 1
        print(n1[0], res)
