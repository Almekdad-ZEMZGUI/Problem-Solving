n = int(input())
for i in range(n):
    line = input().split()
    a = int(line[0])
    b = float(line[1])
    bpm = (60 * a) / b
    aver = 60 / b
    print("%.4f %.4f %.4f" % (bpm - aver, bpm, bpm + aver))
