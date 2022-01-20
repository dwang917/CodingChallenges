line = input("")
gold, silver, copper = line.split()
power = 3*int(gold) + 2*int(silver) + int(copper)

victory = ""
treasure = ""

if(power >= 8):
  victory = "Province"
  treasure = "Gold"
elif(power >= 5):
  victory = "Duchy"
  if(power >= 6):
    treasure = "Gold"
  else:
    treasure = "Silver"
elif(power >= 2):
  victory = "Estate"
  if(power >= 3):
    treasure = "Silver"
  else:
    treasure = "Copper"
else:
  treasure = "Copper"

if(len(victory) != 0):
  print(victory + " or " + treasure)
else:
  print(treasure)
