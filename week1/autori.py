line = input("")
ans = line[0]

for i in range(1, len(line)):
  if line[i] == '-':
    ans+= line[i+1]

print(ans)