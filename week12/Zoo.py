list = []

#parse the input
for i in range(5):
  #make animals into lists based on which list they're in
  subList = []
  n = int(input(""))

  if n!= 0:

    for j in range(n):
      line = input("")
      #getting the type of animal by getting the last word, and normalize into lower case
      animal = line.split()[-1].lower()
      subList.append(animal)
    #now we have a list of sublists of animals
    list.append(subList)
  
  else:
    break

#use of map, function takes a sublist and its index
def countList(list, index):

  dict = {}
  #if the animal is already in the map, increment the count, if not, initialize the count to 1
  for item in list:
    if item in dict:
      dict[item] += 1
    else:
      dict[item] = 1

  print("List " + str(index + 1) + ":")
  # print according to the keys' alphabetical order
  for key in sorted(dict):
    print(key + " | " + str(dict[key]))


#calling the function with each sublist
for index, sublist in enumerate(list):
  countList(sublist, index)