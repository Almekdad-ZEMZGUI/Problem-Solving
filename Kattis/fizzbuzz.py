a = input()
b = a.split(" ")
x = int(b[0])
y = int(b[1])
n = int(b[2])
for i in range(1, n+1):
     if i % x == i % y == 0:
          print("FizzBuzz")
     elif i%x == 0:
          print('Fizz')
     elif i%y == 0:
          print("Buzz")
     else:
          print(i)
