import datetime

n = input().split()
a = datetime.datetime(2009, int(n[1]), int(n[0]))
print(a.strftime('%A'))
