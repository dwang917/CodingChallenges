instruction = input("")
count = input("")
count = int(count)
startingID = input("")
print("")


def check(instruction, startingID, count):
  #checking instruction
  if(instruction != "assign"):
    print("Only assign operation is allowed")
  else:

    #preliminary checking on ID length
    if(len(startingID) != 6):
      print("Wrong starting ID length, please try again")
    else:

      #count checking
      if(count < 1):
        print("count needs to be greater than 0")
      else:

        #checking on reserved bits, need to be 00
        RR = startingID[0:2]
        if(RR != "00"):
          print("Wrong reserved bits, should be 00")
        else:

          II = startingID[3:5]
          
          #checking on II bits, needs to be a non-negative valid hex number
          try:
            II = int(II, 16)
          except:
            print("the identifier is not a valid hexadecimal number")
          else:
            if(II < 0):
              print("identifier needs to be non-negative")
            else:
            
              #checking if overflow occurs with the given count
              if(II + count > 255):
                print("identifier overflow, check your count")
              else:

                #at this point, the input should be ok, so we can go ahead and print all the assigned IDs. I did not perform checking on D and K because there was no specific requirements for them. I took that as they could be flexible
                for i in range(1, count + 1):
                  print(startingID[0:3] + format(II + i, '02X') + startingID[5])


check(instruction, startingID, count)
              
    