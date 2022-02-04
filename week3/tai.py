n = input("")
n = int(n)

samples = []
for i in range(n):
  sample = input("").split()
  #converting into float format to prepare for the math
  sample = [float(item) for item in sample]
  samples.append(sample)

area = 0
for i in range(len(samples) - 1):
  curr = samples[i]
  next = samples[i+1]
  #the math
  area += (curr[1]+next[1])/2 * (next[0]-curr[0])
#unit switching at the end
print(area/1000)
