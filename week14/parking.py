# https://open.kattis.com/problems/parking
# Problem: parking, difficulty: 2.3

#Did not make a function because this problem is easy enough to solve in a few lines of codes

A, B, C = (int(x) for x in input("").split())

list = []

price = 0

# The main idea is to check at every minute how many trucks are parked at that minute, and then calculate the price
for i in range(3):

  arrival, departure = (int(x) for x in input("").split())
  # for each truck, record every single minute the truck is parked in the list
  for i in range(arrival, departure):
    list.append(i)

# From the arrival of the first truck and the departure of the last truck, check the count of every minute in between in the list (the number of trucks parked at that minute), and calculate the price
for i in range(min(list), max(list) + 1):

  if list.count(i) == 1:
    price += A
  
  elif list.count(i) == 2:
    price += B*2
  
  elif list.count(i) == 3:
    price += C*3

print(price)