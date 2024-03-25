n_i = int(input())
n_ii = int(input())
a = (n_i - n_ii) % 360
b =(n_ii - n_i) % 360
if abs(a) < abs(b):
    print(-a)
else:
    print(b)
