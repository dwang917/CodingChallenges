inputs = list(input("").split())
inputs = [int(item) for item in inputs]

for i in range(inputs[2]):
  i = i+1
  if(i % inputs[0] == 0 and i % inputs[1] == 0):
    print("FizzBuzz")
  elif(i % inputs[0] == 0):
    print("Fizz")
  elif(i % inputs[1] == 0):
    print("Buzz")
  else:
    print(i)