t = int(input())
for i in range(t):
    s = input()
    dic = {"r": 0, "u": 0, "b": 0, "y": 0,}
    for c in s:
        if c == "r":
            dic["r"] += 1
        elif c == "u":
            dic["u"] += 1
        elif c == "b":
            dic["b"] += 1
        elif c == "y":
            dic["y"] += 1
    print(min(dic.values()))
