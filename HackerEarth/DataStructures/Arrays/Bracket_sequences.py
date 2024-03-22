s = input()
o, c = 0, 0
 
for i in range(len(s)):
    if s[i] == '(':
        o += 1
    else:
        c += 1
if o != c:
    print(0)
else:
    l = 0
    x = y = 0
 
    for i in range(len(s)):
        if s[i] == ')':
            l += 1
        else:
            l -= 1
 
        if l > y:
            y = l
            x = i + 1
 
    s = s[x:] + s[:x]
    result = 0
    l = 0
 
    for i in range(len(s)):
        if s[i] == '(':
            l += 1
        else:
            l -= 1
        if  l == 0:
            result += 1
    print(result)
