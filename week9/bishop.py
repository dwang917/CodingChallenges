import sys

list = []
for line in sys.stdin:
  line = line.rstrip()
  if line == "":
    break
  list.append(int(line))

#recursive function to solve each board configuration
def bishop(list):

  if(len(list) == 0):
    return

  i = list.pop(0)

  if(i == 0):
    print(0)

  elif(i == 1):
    print(1)

  # math gives the solution to the max # of knights
  else:
    print(2*i - 2)

  bishop(list)

bishop(list)