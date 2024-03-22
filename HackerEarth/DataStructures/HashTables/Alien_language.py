t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    ex = False
    for c in s2:
        if c in s1:
            print("YES")
            ex = True
            break
    if not ex:
        print("NO")
