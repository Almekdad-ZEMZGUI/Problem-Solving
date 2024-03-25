numbers = input().split()
numbers = [int(ele) for ele in numbers]

abc = input()

a = min(numbers)
c = max(numbers)
b = 0
for element in numbers:
     if element != a and element != c:
          b = element

for character in abc:
     if character == "A":
          print(a, end=" ")
     elif character == "B":
          print(b, end=" ")
     else:
          print(c, end=" ")
