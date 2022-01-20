name = input("")
name = list(name)

for i in range(len(name)):
  while(i+1 < len(name) and name[i+1] == name[i]):
    name.pop(i+1)

print("".join(name))