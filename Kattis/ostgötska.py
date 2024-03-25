s = input().split()
per = (len([ele for ele in s if "ae" in ele]) * 100) / len(s)
if per >= 40:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
