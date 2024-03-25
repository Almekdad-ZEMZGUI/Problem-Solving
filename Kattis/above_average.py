c = int(input())
for i in range(c):
    line = [int(e) for e in input().split()]
    avr = sum(line[1:]) / line[0]
    num_stud = 0
    for ele in line[1:]:
        if ele > avr:
            num_stud += 1
    res = (num_stud * 100) / line[0]
    print("%.3f%%" % res)
