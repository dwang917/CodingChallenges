from itertools import permutations


def findApplicablePath(list):
  perm = permutations(list)  #by doing some research, it seems like itertool's permutation is O(n!), n is always 4, so O(24)

  possibleRec = []

  for rec in perm: #O(n!)
    if(rec[0] >= rec[2] and rec[1] <= rec[3]):
      possibleRec.append(rec)
  
  return(possibleRec)
  # so findApplicablePath is O(n!) (O(24))

def findMaxArea(list):
  currArea = -1
  for rec in list: #at most 24 configurations, so O(24)
    if(rec[2] * rec[1] > currArea):
      currArea = rec[2] * rec[1]
  
  return currArea
  # so findMaxArea is O(24)

list = [int(x) for x in input("").split()]
print(findMaxArea(findApplicablePath(list)))
#So the total complexity is O(1) (constant)