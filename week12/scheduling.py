# I didn't make a function for this problem because there's not a lot of code reusing in the problem and it's simple enough using a few lines of code

dict = {}

n = int(input(""))

for i in range(n):
  line = input("").split()
  name = line[:2]
  course = line[-1]
  #check if the course is already in the map
  #if yes, check if the name is in the values of that class, if not, append the name
  if course in dict:
    if name not in dict[course]:
      dict[course].append(name)
  # if no, initialize the course and append the name to that course
  else:
    dict[course] = [name]

# sort the key in alphabetical order and print out the course name and # of people in it.
for course in sorted(dict):
  print(course + " " + str(len(dict[course])))