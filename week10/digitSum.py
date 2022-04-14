#This solution works, but on the given input, it ran out of recursion depth for the third line and failed, so I didn't put it into kattis because I knew it wouldn't pass

#parse the input for each line
n = int(input(""))
list = []
for i in range(n):
  list.append([int(x) for x in input("").split()])

#give the digit sum for a single number
def slice(n):
  sum = 0
  while n != 0:
    sum += n%10
    n = int(n/10)
  return sum

#the recursive solution
def digitSum(start, end, sum):
  #base case
  if start == end:
    sum += slice(start)
    return sum
  #calling the function recursively from start to end
  sum += digitSum(start + 1, end, sum)
  # calculates the sum from the bottom to the current level
  return sum + slice(start)

#call the function for each line
for item in list:
  print(digitSum(item[0], item[1], 0))

  

