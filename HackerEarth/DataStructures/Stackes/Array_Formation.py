import math
def is_prime(ele):
    if ele == 2:
        return True
    if ele % 2 == 0:
        return False
    s = int(math.sqrt(ele) + 1)
    for i in range(3, s, 2):
        if ele % i == 0:
            return False
    return True
 
 
n = int(input())
arr = [int(e) for e in input().split()]
que = []
stack = []
for i in range(len(arr)-1, -1, -1):
    if not is_prime(arr[i]):
        stack.append(arr[i])
    else:
        que.insert(0, arr[i])
 
 
print(*que)
print(*stack)
