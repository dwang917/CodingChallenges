# https://open.kattis.com/problems/abc
# problem: ABC, difficulty: 1.9

ABC = [int(x) for x in input("").split()]
order = input("")
# sort it into ABC order
ABC.sort()
ans = []

# choose the number according to the order
for i in range(3):

  if order[0] == "A":
    ans.append(ABC[0])

  elif order[0] == "B":
    ans.append(ABC[1])

  else:
    ans.append(ABC[2])
  
  order = order[1:]

for x in ans:
  print(x, end=" ")