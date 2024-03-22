s = input()
dic = {}
for c in s:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
vm = 0
km = ""
for k, v in dic.items():
    if v > vm:
        vm = v
        km = k
    elif v == vm:
        km += k
if len(km) == 1:
    print(km, vm)
else:
    min_ords = min([ord(c) for c in km])
    print(chr(min_ords), vm)
