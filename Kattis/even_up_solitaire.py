n = int(input())
arr = [int(e) for e in input().split()]
stack = [arr[0]]
for i in range(1, n):
    if stack and (arr[i] + stack[-1]) % 2 == 0:
        stack.pop()
    else:
        stack.append(arr[i])
print(len(stack))
