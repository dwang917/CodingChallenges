from itertools import permutations


def sortingFunc(item):
  return(item[1])

def find100(list):
  allPerm = permutations(list) #O(n!), because n is always 9, so O(1)

  for perm in allPerm: #O(n!), because n is always 9, so O(1)
    sum = 0
    for i in range(7): #O(1)
      sum += perm[i][0]
    
    if sum == 100:
      ans = perm[0:7]
      ans = sorted(ans, key=sortingFunc) #O(nlogn), because n is always 7, so O(1)
      for i in range(7): #O(1)
        print(perm[i][0])
      return

list = []
for i in range(9):
  list.append([int(input("")), i])

find100(list)
# because the input size is guarenteed to be 9, and there is only one solution with 7 outputs, the program runs in constant time
    
