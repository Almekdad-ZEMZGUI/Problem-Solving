n = int(input())
for i in range(n):
     st = ''
     s = input()
     if s[0] == 'P':
          print('skipped')
     else:
          for ele in s:
               if ele == '+':
                    st += ' '
               else:
                    st += ele
          stt = st.split()
          print(int(stt[0]) + int(stt[1]))
