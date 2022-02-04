import string

dict = {}
reverse_dict = {}
#get a string of the alphabet we're going to use
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
#create 2 dictionaries, one from letter to number, one from number to letter
for i in range(len(alphabet_list)):
  dict[alphabet_list[i]] = i
  reverse_dict[i] = alphabet_list[i]
#DIVIDE
msg = input("")
first_half = msg[:int(len(msg)/2)]
second_half = msg[int(len(msg)/2):]
#ROTATE
def rotate(list):
  sum = 0
  pos = []
  #calculate the sum by looking up the value in the dictionary
  for i in range(len(list)):
    sum += dict[list[i]]
    #also record the current positions of the letters we are going to shift
    pos.append(dict[list[i]])
  after_rotate = ""
  for i in range(len(pos)):
    #calculate the positions after shifting, then look up the corresponding letters in the reverse dictionary
    after_index = (pos[i] + sum) % 26
    after_rotate += reverse_dict[after_index]
  return after_rotate

first_after_rotate = rotate(first_half)
second_after_rotate = rotate(second_half)
#MERGE
after_merge = ""
for i in range(len(first_after_rotate)):
  #look up the positions after merging by checking the dictionary, then convert the positions back to the after-merge letters by checking the reverse dictionary
  merged_index = (dict[first_after_rotate[i]] + dict[second_after_rotate[i]]) % 26
  after_merge += reverse_dict[merged_index]

print(after_merge)