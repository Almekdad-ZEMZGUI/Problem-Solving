n = int(input())
arr_a = [int(e) for e in input().split()]
arr_b = [int(e) for e in input().split()]
 
an = 0
bn = 0
asm = 0
bsm = 0
 
for i in range(n):
    if arr_a[i] == -1:
        an += 1
    else:
        asm += arr_a[i]
    if arr_b[i] == -1:
        bn += 1
    else:
        bsm += arr_b[i]
if an == bn:
    print("Infinite")
elif asm >= bsm and an > 0 :
    print(0)
elif bsm >= asm and bn > 0 :
    print(0)
elif asm < bsm and an == 1:
    print(1)
elif asm > bsm and bn == 1:
    print(1)
elif asm < bsm and an == 2:
[I    print(bsm-asm + 1)
elif asm > bsm and bn == 2:
    print(asm-bsm + 1)
