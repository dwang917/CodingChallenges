line = input("")
length = int(len(line)/3)
msg = line[0:length]
if(msg == line[length:length+length]):
  print(msg)
elif(msg == line[length*2:length*3]):
  print(msg)
else:
  print(line[length:length*2])