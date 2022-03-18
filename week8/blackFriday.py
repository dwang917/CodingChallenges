def winner(list):
  for i in range(6,0,-1): #O(1)
    if list.count(i) == 1: #O(n)
      return list.index(i) + 1 #O(n)
  
  return "none"
  # so this function is O(n)

n = input("")
list = [int(x) for x in input("").split()] #O(n)
print(winner(list))

#So program runs is O(n)