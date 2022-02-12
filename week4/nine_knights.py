from cmath import sqrt
import math


# invalid_dist = sqrt(5)
# board_len = 5

# board = []
# for i in range(board_len):
#     line = input("")
#     board.append(line)

#If two knights conflict, the distance between them must be sqrt(5), so 
#by simply calculating the distances between each knight we will know if two are conflicting
def check(board):
    invalid_dist = sqrt(5)
    board_len = 5
    knight_pos = []

    #store the positions of every knight
    for i in range(board_len):
        for j in range(board_len):
            if board[i][j] == 'k':
                knight_pos.append([i, j])

    #make sure there're 9 knights
    if len(knight_pos) != 9:
        #print("invalid")
        return("invalid")
    
    #check the distance between each combination of knights
    for i in range(len(knight_pos)):
        for j in range(i+1, len(knight_pos)):
            dx = knight_pos[j][0] - knight_pos[i][0]
            dy = knight_pos[j][1] - knight_pos[i][1]
            if math.hypot(dx, dy) == invalid_dist:
                #print("invalid")
                return("invalid")

    #print("valid")
    return("valid")


#check(knight_pos)
