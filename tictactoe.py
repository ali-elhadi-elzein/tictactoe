# 2 players should be able to play the game
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
import os

def screen_clear():
    _ = os.system("cls")
    
    
# board
def change_board(board, number, XorO):
    screen_clear()
    # changes the choosen position with X or O
    board[int(number)-1] = XorO
    print(f"""
          {board[0]}|{board[1]}|{board[2]}
          -----
          {board[3]}|{board[4]}|{board[5]}
          -----
          {board[6]}|{board[7]}|{board[8]}
          """)
    
    return board


def can_handle(player, numbers): 
    
    if player.isdigit() == False:    # check if player input is a digit            
        print("This is not a number\nchoose a number from numbers")
        print("numbers = ", numbers)
    
    if player.isdigit() == True:
        player = int(player)    # convert the input to integer
        
        if player in numbers:   # check if number is valid
            numbers.remove(player)
            return numbers, True
        
        else: 
            print("This number is out of range or have been choosen")
            print("numbers = ", numbers)
    
    return numbers, False

def check_game(board, game_on=True):
    global player1score
    global player2score
    winner = " "
       
    def which_player_won(XorO):
        if XorO == "X":
            return "player1"
        elif XorO == "O":
            return "player2"
    # rows
    if board[0] == board[1] == board[2]:
        print(f"game over\n {which_player_won(board[0])} won")
        winner = board[0]
        game_on = False
    elif board[3] == board[4] == board[5]:
        print(f"game over\n {which_player_won(board[3])} won")
        winner = board[3]
        game_on = False
    elif board[6] == board[7] == board[8]:
        print(f"game over\n {which_player_won(board[6])} won")
        winner = board[6]
        game_on = False

    # columns
    elif board[0] == board[3] == board[6]:
        print(f"game over\n {which_player_won(board[0])} won")
        winner = board[0]
        game_on = False
    elif board[1] == board[4] == board[7]:
        print(f"game over\n {which_player_won(board[4])} won")
        winner = board[1]
        game_on = False
    elif board[2] == board[8] == board[5]:
        print(f"game over\n {which_player_won(board[2])} won")
        winner = board[2]
        game_on = False
        
    # diagonals
    elif board[0] == board[4] == board[8]:
        print(f"game over\n {which_player_won(board[0])} won")
        winner = board[0]
        game_on = False
    elif board[2] == board[4] == board[6]:
        print(f"game over\n {which_player_won(board[2])} won")
        winner = board[2]
        game_on = False
    
    # if numbers list is empty
    elif numbers == []:
        game_on = False
    
    if game_on == False:
        winner = which_player_won(winner)
        if winner == "player1":
            player1score += 1
            print(f"player1 = {player1score}")
            print(f"player2 = {player2score}")
        elif winner == "player2":
            player2score += 1
            print(f"player1 = {player1score}")
            print(f"player2 = {player2score}")
        else:
            print("it is a tie!")
            print(f"player1 = {player1score}")
            print(f"player2 = {player2score}")
            
    return game_on

def take_first_value(value):
    return value[0]

def check_if_want_to_play():
    while True:
        answer = input("Do you want to play again(y/n): ").lower()
        if answer == "y":
            return True

        if answer == "n":
            return False
        
        else: print("Invalid input!") 
            

want_to_play = True
# scoreboard
player1score = 0
player2score = 0

while want_to_play:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_on = True

    # print new canva
    print(f"""
          {board[0]}|{board[1]}|{board[2]}
          -----
          {board[3]}|{board[4]}|{board[5]}
          -----
          {board[6]}|{board[7]}|{board[8]}
          """)
    
    # game runs forever
    while game_on:
        
        # player 1 turn
        while True:
            player1input = input(
    """
    You are 'X'
    Enter position: """)
            numbers, check = can_handle(player1input, numbers)
            if check == True:
                change_board(board, player1input, "X")
                break
            
            
        # check game if over    
        if check_game(board) == False:
            break
        
            
        # player 2 turn
        while True:
            player2input = input(
    """
    You are 'O'
    Enter position: """)
            numbers, check = can_handle(player2input, numbers)
            if check == True:
                change_board(board, player2input, "O")
                break
        
        # check game if over    
        if check_game(board) == False:
            break
        
    # check if want to play another game
    want_to_play = check_if_want_to_play()
    screen_clear()