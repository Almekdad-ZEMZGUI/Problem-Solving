n = int(input())
all_teams = []
for i in range(n):
     line = input().split()
     all_teams.append(line)
m = []
nm = 0
out = []
for j in range(len(all_teams)):
     if all_teams[j][0] in m:
          continue
     else:
          out.append(all_teams[j])
          m.append(all_teams[j][0])
          nm += 1
     if nm == 12:
          break
for ele in out:
     print(ele[0], ele[1])
