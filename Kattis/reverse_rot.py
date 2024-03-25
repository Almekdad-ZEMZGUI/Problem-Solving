while True:
    s = input()
    if s == '0':
        break
    l = s.split()
    st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    stn = ''
    rev = l[1][::-1]
    for ele in rev:
        ind = st.index(ele)
        ind += int(l[0])
        if ind >= len(st):
            ind = ind % len(st)
        stn += st[ind]
    print(stn)
