line = input("")
first, second = line.split()
#using subtring to get the last 2 chars and check if they are ex
if(first[len(first)-2:] == 'ex'):
  print(first + second)
# checking if first name ends with e, if so, simply append x
elif(first[len(first)-1] == 'e'):
  print(first + 'x' + second)
#if first name ends with a,i,o,u, append ex
elif(first[len(first)-1] in ['a', 'i', 'o', 'u']):
  print(first[:len(first)-1] + 'ex' + second)
#all other general case, simply append ex
else:
  print(first + "ex" + second)