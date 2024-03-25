s = input()
stack = []
for ele in s:
    if ele == "<":
        stack.pop()
    else:
        stack.append(ele)

for ele in stack:
    print(ele, end='')
