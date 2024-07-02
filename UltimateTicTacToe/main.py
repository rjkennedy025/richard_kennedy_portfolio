from turtle import Screen
from boards import Board
from logic import Logic
from highlight import Highlight
import time
import sys

play_again = 'yes'
while play_again == 'yes':

    screen = Screen()
    board = Board()
    logic = Logic()
    highlight = Highlight(board.screen_size)

    screen.setup(board.screen_size * 1.1, board.screen_size * 1.1)
    screen.title('Ultimate Tic Tac Toe')
    screen.screensize(board.screen_size, board.screen_size)

    screen.tracer(0)
    board.create_board()
    screen.tracer(1)

    logic.game_start(board.board_details)
    highlight.highlight_board(logic.current_player, logic.current_board, board.board_details)

    while logic.game_over is False:
        screen.tracer(0)
        logic.win_in_round = False
        logic.find_available_boards(board.board_details)
        logic.player_choice(board.board_details)
        board.place_marker(logic.current_player, logic.current_board, logic.current_choice)
        logic.win_subboard_check(board.board_details)
        if logic.win_in_round is True:
            board.subboard_winning_line(logic.current_player, logic.current_board, logic.subboard_winning_sequence)
            logic.win_mainboard_check(board.board_details)
            if logic.game_over is True:
                board.mainboard_winning_line(logic.current_player, logic.mainboard_winning_sequence)
        logic.draw_game(board.board_details)
        logic.next_turn(logic.current_choice)
        highlight.highlight_board(logic.current_player, logic.current_board, board.board_details)
        highlight.highlight_square(logic.current_player, logic.prior_board, logic.prior_choice, board.board_details)
        screen.tracer(1)

    play_again = input('Would you like to play again? Yes or No: ').lower().strip()
    while play_again not in ['yes', 'no']:
        play_again = input(
            f'Sorry, {play_again} is not valid. Would you like to play again? Yes or No: ').lower().strip()

    if play_again == 'yes':
        screen.clear()
    elif play_again == 'no':
        print('Goodbye')
        time.sleep(1)
        sys.exit()
# End of Play Again While Loop
