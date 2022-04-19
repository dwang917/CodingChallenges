from hashlib import new


# I know this function smells from HW5 but it's working as intended and it's not the main purpose of this HW so I just left it as it was for the time being to avoid building everything up from scratch again
def assign(count, startingID):
    print("")
  # checking instruction
    # preliminary checking on ID length
    if(len(startingID) != 6):
        print("Wrong starting ID length, please try again")
    else:

        # count checking
        if(count < 1):
            print("count needs to be greater than 0")
        else:

            # checking on reserved bits, need to be 00
            RR = startingID[0:2]
            if(RR != "00"):
                print("Wrong reserved bits, should be 00")
            else:

                II = startingID[3:5]

                # checking on II bits, needs to be a non-negative valid hex number
                try:
                    II = int(II, 16)
                except:
                    print("the identifier is not a valid hexadecimal number")
                else:
                    if(II < 0):
                        print("identifier needs to be non-negative")
                    else:

                        # checking if overflow occurs with the given count
                        if(II + count > 255):
                            print("identifier overflow, check your count")
                        else:

                            # at this point, the input should be ok, so we can go ahead and print all the assigned IDs. I did not perform checking on D and K because there was no specific requirements for them. I took that as they could be flexible
                            for i in range(1, count + 1):
                                print(
                                    startingID[0:3] + format(II + i, '02X') + startingID[5])



# The new defrag-move function
def defrag():
  dc = input("")
  n = int(input(""))
  IDs = []
  for i in range(n):
    IDs.append(input(""))

  print("")
  dict = {}

  for id in IDs:
    k = id[2]
    # using a dictionary to keep track of how many IDs of same k are already in the new DB, so the new I field would simply be the length of dict[k] - 1
    if k not in dict:
      dict[k] = [id]
    else:
      dict[k].append(id)
    #getting the new I field and format it to 3 digits
    newCount = format(len(dict[k]) - 1, '03X')
    #assembling every part to get the new ID
    newID = dc[0] + newCount[0] + k + newCount[1:] + dc[1]
    print(newID)



# decide which action to perform
def decide():
    instruction = input("")

    if instruction == "assign":
      assign(int(input("")), input(""))

    elif instruction == "defrag-move":
      defrag()

    else:
      print("invalid instruction")

# This program solves both this problem and HW5, I tested inputs from both assignments and it worked as intended
decide()
