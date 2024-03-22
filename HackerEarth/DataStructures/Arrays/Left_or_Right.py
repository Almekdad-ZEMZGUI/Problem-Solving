n, q = [int(e) for e in input().split()]
arr = [int(e) for e in input().split()]
arr_set = set(arr)
i = 0
dic = {}
for ele in arr:
    if ele in dic.keys():
        dic[ele].append(i)
    else:
        dic[ele] = [i]
    i += 1
for i in range(q):
    line = input().split()
    y, z, d = int(line[0]), int(line[1]), line[2]
    if z not in dic:
        print(-1)
    else:
        z_indices = dic[z]
        if d == "L":
            dis_min = n
            for e in z_indices:
                if e < y:
                    dis = (y - e) % n
                else:
                    dis = (y + (n - e)) % n
                dis_min = min(dis, dis_min)
        else:
            dis_min = n
            for e in z_indices:
                if e < y:
                    dis = ((n - y) + e) % n
                else:
                    dis = (e - y) % n
                dis_min = min(dis, dis_min)
        print(dis_min)
