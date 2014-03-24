import re
from board import GameBoard
from players import Player

"""
  Prompt user for number of human players
"""
def get_num_humans():
    input_check = re.compile('[2]')

    valid = False
    while not valid:
        # Get input from user
        num_humans = raw_input()
       
        # Check for valid input
        if (input_check.match(num_humans)):
            valid = True
        else:
            print "Please enter the number 2..."

    return int(num_humans)

"""
  This is the main logic for the game.  It will:
    - create the board
    - prompt for number of players (human/computer)
    - prompt for player names
    - loop - allowing for multiple games for same players
    - loop - for each player move - re-displaying board each time
    - check for winner and display winner name or tie if game over
    - prompt to see if they want to play again
"""
# Create array to hold players
players = []

board = GameBoard()

print "\nWelcome to the TIC-TAC-TOE game!\n"

# Hard code this for now - will prompt later
num_players = get_num_humans() 

player_cnt = 0
# Prompt for player's names and then create player
while player_cnt < num_players:
    # Use static method to get name
    name = Player.get_player_name()

    # Create player and add to player list
    players.append(Player(name, board, player_cnt))
    player_cnt += 1

playing_game = True
while playing_game:
    print board

    moves = 0
    current_player_id = 0
    active_turn = True
    while active_turn:
        moves += 1
        # Grab the current player (based on id)
        player = players[current_player_id]
        
        print "%s's turn: Move #%d...\n" % (player.get_name(), moves)
        
        player.make_move()

        print board

        if moves > 4 and board.check_for_win():
            # If win combo was found, set to winner
            board.winner = player
            active_turn = False
        elif (moves == 9):
            # If max # of moves, done with game
            active_turn = False
        else:
            # Move to the next player
            if (current_player_id == 1):
                current_player_id = 0
            else:
                current_player_id = 1

    if (board.winner):
        print "The WINNER is %s!" % board.winner.get_name()
    else:
        print "It was a TIE game!"

    playing_game = False

