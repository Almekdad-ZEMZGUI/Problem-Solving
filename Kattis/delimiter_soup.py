n = int(input())
s = input()
stack = []
dic = {"(":")", "[":"]", "{":"}"}
notok = True
for i in range(len(s)):
    if s[i] in dic:
        stack.append(s[i])
    elif s[i] in dic.values():
        if stack and dic[stack[-1]] == s[i]:
            stack.pop()
        else:
            print(s[i] + " " + str(i))
            notok = False
            break
if notok:
    print("ok so far")
