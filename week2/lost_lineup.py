from posixpath import split

# I spent a big chunck of time trying to figure out what the input/output meant because
# I understood "the order" wrong. Once figured out the output is arranging the
# order of the indices of the people from the second line, it's fairly easy

#getting the number of people in the line
total = input('')
total = int(total)
#if only Jimmy's in the line, no further actions needed
if(total == 1):
  print(1)
else:
  #getting the number of people between each person and Jimmy
  between = input('')
  between = between.split()
  # convert the list into integer format
  for i in range(len(between)):
    between[i] = int(between[i])
  # we know Jimmy is always the first, so the list starts with 1
  ans = [1]
  # finding the index of the person right next to Jimmy
  curr = 0
  #while we haven't arranged everybody in the line, we keep looking
  while(curr < len(between)):
    for i in range(len(between)):
      # We found the next person, we take the index and plus 2 for placeholding
      if between[i] == curr:
        ans.append(i+2)
    # Now repeat and find the person with 1 other person in between them and Jimmy
    curr +=1
  # print number in the list in a single line
  for i in ans:
    print(i, end=" ")

