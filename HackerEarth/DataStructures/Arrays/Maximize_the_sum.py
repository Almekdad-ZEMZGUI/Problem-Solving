t = int(input())
for i in range(t):
    n, k = [int(ele) for ele in input().split()]
    arr = [int(ele) for ele in input().split() if int(ele) > 0]
    num_mapping = {}
    for number in arr:
        if number not in num_mapping:
            num_mapping[number] = number
        else:
            num_mapping[number] += number
    if len(num_mapping) <= k:
        result = sum(num_mapping.values())
    else:
        result = sum(sorted(num_mapping.values())[-k:])
    print(result)
