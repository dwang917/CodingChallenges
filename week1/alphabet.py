line = input("")
length = len(line)

space = 0
upper = 0
lower = 0
symb = 0

for i in range(length):
  now = line[i]
  if now == '_':
    space+=1
  elif now.isupper():
    upper+=1
  elif now.islower():
    lower+=1
  else:
    symb+=1

print(space/length)
print(lower/length)
print(upper/length)
print(symb/length)
