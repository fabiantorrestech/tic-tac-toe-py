def print_rules():
    print("Welcome to my TicTacToe Project!\n\n")
    print("To exit the program while running, press Ctrl+C at any time.\n\n")
    print("RULES:")
    print("- Player 1 is X's. Player 2 is O's\n- Simply type a coordinate within parenthesees to choose a spot on the board, like so.\n")
    print("- (#Row,#Column) \n- Rows range from [0,2] (left to right), while columns range from [0,2] (top to bottom).\n")
    print("- For example, to choose the top left spot, type (0,0). To choose bottom right, type (2, 2). To choose middle left, (1, 0)\n\n")
    print("MODES: ")
    print("1) 2 Player")
    #print("2) vs CPU\n")

def check_win(grid):

    # ------ X's cases -----

    #1) down left column
    if( grid[0] == 'X' and grid[3] == 'X' and grid[6] == 'X'):
        return 1
    #2) down middle column
    elif( grid[1] == 'X' and grid[4] == 'X' and grid[7] == 'X'):
        return 1
    #3) down right column
    elif( grid[2] == 'X' and grid[5] == 'X' and grid[8] == 'X'):
        return 1
    #4) diagonal top left to bottom right
    elif( grid[0] == 'X' and grid[4] == 'X' and grid[8] == 'X'):
        return 1
    #5) diagonal top right to bottom left
    elif( grid[2] == 'X' and grid[4] == 'X' and grid[6] == 'X'):
        return 1
    #6) top row
    elif( grid[0] == 'X' and grid[1] == 'X' and grid[2] == 'X'):
        return 1
    #7) middle row
    elif( grid[3] == 'X' and grid[4] == 'X' and grid[5] == 'X'):
        return 1
    #8) bottom row
    elif( grid[6] == 'X' and grid[7] == 'X' and grid[8] == 'X'):
        return 1

     # ------ O's cases -----
    #1) down left column
    if( grid[0] == 'O' and grid[3] == 'O' and grid[6] == 'O'):
        return 1
    #2) down middle column
    elif( grid[1] == 'O' and grid[4] == 'O' and grid[7] == 'O'):
        return 1
    #3) down right column
    elif( grid[2] == 'O' and grid[5] == 'O' and grid[8] == 'O'):
        return 1
    #4) diagonal top left to bottom right
    elif( grid[0] == 'O' and grid[4] == 'O' and grid[8] == 'O'):
        return 1
    #5) diagonal top right to bottom left
    elif( grid[2] == 'O' and grid[4] == 'O' and grid[6] == 'O'):
        return 1
    #6) top row
    elif( grid[0] == 'O' and grid[1] == 'O' and grid[2] == 'O'):
        return 1
    #7) middle row
    elif( grid[3] == 'O' and grid[4] == 'O' and grid[5] == 'O'):
        return 1
    #8) bottom row
    elif( grid[6] == 'O' and grid[7] == 'O' and grid[8] == 'O'):
        return 1

    return 0

def process_location(grid, location, piece):
    if( len(location) < 5 or location.find("(") == -1 or location.find(")") == -1 or location.find(",") == -1 ):
        print("User_input is badly formatted, try again!")
        return 0

    location = location.replace("(", "")
    location = location.replace(")", "")
    
    #check that the numbers in the paranthesees are within [0,2]
    if(int(location[0]) <= 2 and int(location[0]) >= 0):
        if(int(location[2]) <= 2 and int(location[2]) >= 0):
            #start doing stuff
            if(int(location[0]) == 0 and int(location[2]) == 0):
                if(grid[0] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[0] = piece
            elif(int(location[0]) == 0 and int(location[2]) == 1):
                if(grid[1] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[1] = piece
            elif(int(location[0]) == 0 and int(location[2]) == 2):
                if(grid[2] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[2] = piece
            elif(int(location[0]) == 1 and int(location[2]) == 0):
                if(grid[3] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[3] = piece
            elif(int(location[0]) == 1 and int(location[2]) == 1):
                if(grid[4] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[4] = piece
            elif(int(location[0]) == 1 and int(location[2]) == 2):
                if(grid[5] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[5] = piece
            elif(int(location[0]) == 2 and int(location[2]) == 0):
                if(grid[6] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[6] = piece
            elif(int(location[0]) == 2 and int(location[2]) == 1):
                if(grid[7] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[7] = piece
            elif(int(location[0]) == 2 and int(location[2]) == 2):
                if(grid[8] != "-"):
                    print("That spot is already taken, buddy, nice try! (:")
                    return 0
                else:
                    grid[8] = piece
        else:
            return 0
    else:
        return 0
    return 1

    


def player_turn(grid, player_num):
    piece = "X"
    good_input = 0
    if(player_num == 1):
        piece = "X"
    if(player_num == 2):
        piece = "O"
    while(good_input != 1):
        location = input("Player "+ str(player_num) + ", Where would you like to place your piece?")

        #returns 0 if user_input is formatted badly!
        #returns 1 upon good input!
        good_input = process_location(grid, location, piece)
    

def create_grid(grid):
    print( grid[0], " | ", grid[1], " | ", grid[2])
    print("___|_____|____")
    print( grid[3], " | ", grid[4], " | ", grid[5])
    print("___|_____|____")
    print( grid[6], " | ", grid[7], " | ", grid[8], "\n", "\n")


def main():
    print_rules()
    user_option = int(input("Enter a mode: "))
    grid = [ "-", "-", "-", "-", "-", "-", "-", "-", "-" ]
    player_num = 1

    if(user_option == 1):
        turns = 0
        while turns < 9:
            #check_win will return 1 upon a winner

            winner = check_win(grid)
            if(winner == 1):
                print("Game Ended! Player " + str(player_num) + " is the winner!")
                create_grid(grid)
                return

            create_grid(grid)
            player_turn(grid, player_num)
            
            # player 2  = odd turns (1, 3, 5, 7, 9)
            # player 1 = even turns (0, 2, 4, 6, 8)
            if(player_num == 2):
                player_num = 1
            else:
                player_num = 2
            turns += 1
            

        

    #elif(user_option == 2):
    #    create_grid(grid)




# always include this because it will make sure to run our main.
if __name__ == "__main__":
    main()
