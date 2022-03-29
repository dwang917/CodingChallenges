import sys


n = int(input(""))
list = []

for i in range(n):
  list.append(int(input("")))

#recursive function to print the list in reversed order
def reverse(list):

  if(len(list) == 0):
    return

  print(list.pop())

  reverse(list)


reverse(list)
