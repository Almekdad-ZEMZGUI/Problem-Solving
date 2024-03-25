while True:
    s = input()
    if s == '0':
        break
    s = s.split()
    print(((abs((float(s[0]) - float(s[2]))) ** float(s[4])) + (abs((float(s[1]) - float(s[3]))) ** float(s[4]))) ** (1/float(s[4])))
