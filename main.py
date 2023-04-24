from board import Board
from game import Game
import os


def main():
    tic_tac_board = Board()
    tic_tac_game = Game(tic_tac_board.board)
    tic_tac_board.show_board()
    tic_tac_game.starting_player()
    for i in range(9):
        #os.system('printf \'\\33c\\e[3J\'')
        tic_tac_board.show_board()
        tic_tac_game.player_move()
        if tic_tac_game.round_counter >= 5:
            tic_tac_game.get_winner()

    print("It's a draw")
main()




