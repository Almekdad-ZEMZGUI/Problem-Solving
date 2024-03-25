n = input().split()
l = []
for i in range(int(n[1])):
    l.append(int(input()))
if int(n[0]) == int(n[1]):
    print('too late')
else:
    for i in range(1, int(n[0]) + 1):
        if i not in l:
            print(i)
            break
