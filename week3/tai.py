n = input("")
n = int(n)

samples = []
for i in range(n):
  sample = input("").split()
  sample = [float(item) for item in sample]
  samples.append(sample)

area = 0
for i in range(len(samples) - 1):
  curr = samples[i]
  next = samples[i+1]
  area += (curr[1]+next[1])/2 * (next[0]-curr[0])

print(area/1000)
