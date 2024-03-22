t = int(input())
 
for i in range(t):
    n, p, q, r = [int(e) for e in input().split()]
    pth = set(i for i in range(p, n + 1, p))
    qth = set(i for i in range(q, n + 1, q))
    rth = set(i for i in range(r, n + 1, r))
 
    p_only = pth.difference(qth).difference(rth)
    q_only = qth.difference(pth).difference(rth)
    r_only = rth.difference(pth).difference(qth)
 
    print(len(p_only) + len(q_only) + len(r_only))
