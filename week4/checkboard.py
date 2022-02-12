# commented out input manipulation for the purpose of unit test (not sure if there's a better way)

# n = int(input(""))
# grid = []
# for i in range(n):
#     line = input("")
#     grid.append(line)

# pass in the list of board configuration as grid
def check_checkboard(grid):

    n = len(grid)
    # this for loop checks horizontal conditions
    for line in grid:

        same_color_count = 1
        black_count = 0
        white_count = 0
        # loop through each line of the board
        for i in range(n):

            if line[i] == 'B':
                black_count += 1
            else:
                white_count += 1

            # if the next piece is same color, increment the count
            if i < n - 1:
                if line[i + 1] == line[i]:
                    same_color_count += 1
                # if different color, reset the count
                else:
                    same_color_count = 1

            # modified for unittest
            if same_color_count == 3:
                # print(0)
                return(0)

        if(black_count != white_count):
            # print(0)
            return(0)

    # This for loop checks vertical conditions
    for i in range(n):
        same_color_count_vert = 1
        black_count_vert = 0
        white_count_vert = 0

        # This nested for loop checks each piece in the same vertical line at index i
        for j in range(n):

            if grid[j][i] == 'B':
                black_count_vert += 1
            else:
                white_count_vert += 1

            if j < n - 1:
                if grid[j][i] == grid[j+1][i]:
                    same_color_count_vert += 1
                else:
                    same_color_count_vert = 1

            if same_color_count_vert == 3:
                # print(0)
                return(0)

        #after checking the vertical line, check the number condition      
        if(black_count_vert != white_count_vert):
            # print(0)
            return(0)
            
    # print(1)
    return(1)

# check_checkboard(grid)
