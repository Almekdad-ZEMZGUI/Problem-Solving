n = input().split()
def f(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l
while n != ['1', '2', '3', '4', '5']:
    for i in range(4):
        if int(n[i]) > int(n[i+1]):
            n = f(n, i, i + 1)
            for ele in n:
                if ele == n[-1]:
                    print(ele, end='')
                else:
                    print(ele, end=' ')
            print()
