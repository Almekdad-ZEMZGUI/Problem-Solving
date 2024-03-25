N = int(input())
for i in range (N):
     G = int(input())
     guests=input().split()
     for ele in guests:
          if guests.count(ele)==1:
               print('Case #%d: %s' %(i+1,ele))
               break
