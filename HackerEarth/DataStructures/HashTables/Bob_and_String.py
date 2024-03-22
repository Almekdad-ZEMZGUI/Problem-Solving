n = int(input())
for i in range(n):
    s = input()
    t = input()
    s_dic = {}
    t_dic = {}
    for c in s:
        if c in s_dic:
            s_dic[c] += 1
        else:
            s_dic[c] = 1
    for c in t:
        if c in t_dic:
            t_dic[c] += 1
        else:
            t_dic[c] = 1
    count = 0
    for k in s_dic:
        if k not in t_dic:
            count += s_dic[k]
        else:
            count += abs(s_dic[k] - t_dic[k])
    for k in t_dic:
        if k not in s_dic:
            count += t_dic[k]
 
    print(count)
