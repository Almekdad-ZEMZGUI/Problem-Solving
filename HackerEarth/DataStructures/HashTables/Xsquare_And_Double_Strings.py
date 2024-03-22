t = int(input())
for i in range(t):
    s = input()
    sett = set(s)
    if len(sett) == len(s):
        print("No")
    else:
        print("Yes")
