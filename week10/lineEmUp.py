n = int(input(""))

list = []
#getting all the names into a list
for i in range(n):
  list.append(input(""))

# the recursive function
def checkOrder(list, order, n):
  #base case, when we at the last name, no checking needs to be performed
  if(len(list) == 1):
    # if the order is incremented by 1 by all the preceding names, we know it's in increasing order
    if order == n - 1:
      print("INCREASING")
    #same idea for decreasing order
    elif order == -n + 1:
      print("DECREASING")
    # if neither, then we know it's neither
    else:
      print("NEITHER")
    
    return

  now = list.pop()
  #if the current name is bigger than the next name. increment the count
  if now > list[0]:
    order += 1
  #if not, decrement the count
  elif now < list[0]:
    order -= 1
  # calling the function recursively with updated list and count
  checkOrder(list, order, n)

order = 0
checkOrder(list, order, n)