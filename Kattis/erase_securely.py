n = int(input())
s1 = input()
s2 = input()
if n % 2 == 0:
    if s1 == s2:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    res = 0
    for i in range(len(s1)):
        if (s1[i] == '1' and s2[i] == '0') or (
            s1[i] == '0' and s2[i] == '1'):
            res += 1
    if res == len(s1):
        print('Deletion succeeded')
    else:
        print('Deletion failed')
