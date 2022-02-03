rooms = input("")
teams = input("")
rooms = int(rooms)
teams = int(teams)

arrangement = []
mod = teams % rooms
for i in range(rooms):
 arrangement.append(int(teams/rooms))

for i in range(mod):
  arrangement[i] += 1

for i in range(len(arrangement)):
  i_line = '*'*arrangement[i]
  print(i_line)
