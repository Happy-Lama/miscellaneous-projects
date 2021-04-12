import random

playing_controls = "1 2 3 4 5 6 7 8 9".split(" ")

def print_board(playing_squares):

    #prints the playing board with the relevant plays made
    
    for idx, i in enumerate(playing_squares):
        if idx < 2:
            print(" ",i," |",end='')
        elif idx == 2:
            print(" ",i)
            print("-----|-----|-----")
        elif idx < 5:
            print(" ",i," |",end='')
        elif idx == 5:
            print(" ",i)
            print("-----|-----|-----")
        elif idx < 8:
            print(" ",i," |",end='')
        elif idx == 8:
            print(" ",i)
            
    
def winner(player_plays,computer_plays):

    #computes who the winner is from their plays made

    #winning combinations

    rows = ('123','456','789')
    columns = ('149','258','369')
    diagonals = ('159','357')
    
    if any((player_plays in i for i in [rows,columns,diagonals])):
        return "Player Win"
    elif any((computer_plays in i for i in [rows,columns,diagonals])):
        return "Computer Win"
    else:
        return "Draw"
        
def start_game():

    #mainloop for gameplay 

    while True:
        print("To access/play in a particular cell, type:",playing_controls)
        
        player_plays = ""
        computer_plays = ""
        
        while len(player_plays) != 3:
            print_board(playing_squares)
            user_input = input()
            while playing_squares[int(user_input) - 1] in "XO":
                user_input = input()
            playing_squares[int(user_input) - 1] = "X"
            player_plays += user_input
            computer_play = str(random.randint(0,8))
            while playing_squares[int(computer_play)] in "XO":
                computer_play = str(random.randint(0,8))
                
            playing_squares[int(computer_play)] = "O"
            computer_plays += str(int(computer_play) + 1)
            
        print(player_plays)
        print(computer_plays)
        print_board(playing_squares)
        print(winner(player_plays,computer_plays))
        
        break

while True:
    playing_squares = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    print("Enter S to start and Q to quit")
    user_input = input()
    
    if user_input == "S":
        start_game()
    if user_input == "Q":
        break
