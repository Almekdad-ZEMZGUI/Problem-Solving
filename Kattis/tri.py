n = input().split()
a ,b ,c = int(n[0]), int(n[1]), int(n[2])
if a - b == c:
     print('{}-{}={}'.format(a,b,c))
elif a == b - c:
     print('{}={}-{}'.format(a,b,c))
elif a + b == c:
     print('{}+{}={}'.format(a,b,c))
elif a == b + c:
     print('{}={}+{}'.format(a,b,c))
elif a == b * c:
     print('{}={}*{}'.format(a,b,c))
elif a * b == c:
     print('{}*{}={}'.format(a,b,c))
[Ielif a == b / c:
     print('{}={}/{}'.format(a,b,c))
elif a / b == c:
     print('{}/{}={}'.format(a,b,c))
