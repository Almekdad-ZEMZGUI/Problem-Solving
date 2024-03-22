n, m = [int(element) for element in input().split()]
menus = []
for i in range(n):
    menus.append([int(element) for element in input().split()])
 
max_columns = set()
for j in range(m):
    max_columns.add(max(menus[i][j] for i in range(n)))
 
menus_with_max = {i: 0 for i in range(n)}
 
for i in range(n):
    for price in menus[i]:
        if price in max_columns:
            menus_with_max[i] += 1
 
max_value = max(menus_with_max.values())
 
menus_with_max_value = [i for i, v in menus_with_max.items() if v == max_value]
 
if len(menus_with_max_value) == 1:
    print(menus_with_max_value[0] + 1)
else:
    dic_sums = {i: sum(menus[i]) for i in menus_with_max_value}
    max_sum = max(dic_sums.values())
    menu_with_max_sum = [i for i, v in dic_sums.items() if v == max_sum]
    print(menu_with_max_sum[0] + 1)
