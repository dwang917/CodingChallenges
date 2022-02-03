import string

dict = {}
reverse_dict = {}

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

for i in range(len(alphabet_list)):
  dict[alphabet_list[i]] = i
  reverse_dict[i] = alphabet_list[i]

msg = input("")
first_half = msg[:int(len(msg)/2)]
second_half = msg[int(len(msg)/2):]

def rotate(list):
  sum = 0
  pos = []
  for i in range(len(list)):
    sum += dict[list[i]]
    pos.append(dict[list[i]])
  after_rotate = ""
  for i in range(len(pos)):
    after_index = (pos[i] + sum) % 26
    after_rotate += reverse_dict[after_index]
  return after_rotate

first_after_rotate = rotate(first_half)
second_after_rotate = rotate(second_half)

after_merge = ""
for i in range(len(first_after_rotate)):
  merged_index = (dict[first_after_rotate[i]] + dict[second_after_rotate[i]]) % 26
  after_merge += reverse_dict[merged_index]

print(after_merge)