rooms = input("")
teams = input("")
rooms = int(rooms)
teams = int(teams)

arrangement = []
#left-over teams we will have
mod = teams % rooms
for i in range(rooms):
  #first assign the max equal number of teams to each room
 arrangement.append(int(teams/rooms))
# for the left-over teams, assign to each team in order
for i in range(mod):
  arrangement[i] += 1

for i in range(len(arrangement)):
  i_line = '*'*arrangement[i]
  print(i_line)
