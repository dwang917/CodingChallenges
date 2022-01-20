word = input("")
found = False

for i in range(len(word)):
  for j in range(i+1, len(word)):
    if(word[i] == word[j]):
      print("0")
      found = True
      break
  if found:
    break

if(not found):
  print("1")
    