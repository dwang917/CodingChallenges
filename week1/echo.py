n = input("")
n = int(n)

list = []
for i in range(n):
  word = input("")
  list.append(word)

i = 0
while(i <= n-1):
  print(list[i])
  i+= 2