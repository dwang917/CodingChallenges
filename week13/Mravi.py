import math

n = int(input(""))
list = []
tail = []

for i in range(n-1):
  line = [int(x) for x in input("").split()]
  list.append(line)
  #keep a copy of the end of a pipe for later lookup
  tail.append(line[1])

leaves = [int(x) for x in input("").split()]

minimum = -1

#iterate thru the leaves
for index, liter in enumerate(leaves):

  if liter != -1:
    # index+1 is the nth leaf, look up the pipe that ends with that leaf
    pipe = list[tail.index(index+1)]

    #if we haven't traveled to the first pipe yet, keep looking up the previous pipe
    while pipe[0] != 1:
      # if superpipe, take the sqrt
      if pipe[-1] == 1:
        liter = math.sqrt(liter)
      
      liter = liter/(pipe[2]/100)
      # use the start node of the current pipe to look up the previous pipe where the end node is the same
      pipe = list[tail.index(pipe[0])]

    # in case the first pipe is a superpipe, do an additional check
    if pipe[-1] == 1:
        liter = math.sqrt(liter)
    
    liter = liter/(pipe[2]/100)
    # update the current minimum liquid needed
    if liter > minimum:
      minimum = liter

print(format(minimum, '.3f'))
    
