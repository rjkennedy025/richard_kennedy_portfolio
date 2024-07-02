import random
from time import sleep

WINNING_SEQUENCES = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],
                     ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],
                     ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1']]
RULES = "If you've never played before, visit https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe for the rules"


class Logic:
    def __init__(self):
        self.player_count = ''
        self.current_player = 'X'
        self.current_board = ''
        self.prior_board = ''
        self.available_squares = []
        self.available_boards = []
        self.current_choice = ''
        self.prior_choice = ''
        self.win_in_round = False
        self.game_over = False
        self.winning_sequences = WINNING_SEQUENCES
        self.subboard_winning_sequence = []
        self.mainboard_winning_sequence = []

    def game_start(self, board_details):
        print('The game is Ultimate Tic Tac Toe!')
        print(RULES)
        valid_player_count = False
        while valid_player_count is False:
            self.player_count = input('How many players: 1 or 2? ').strip()
            if self.player_count in ['1', '2']:
                valid_player_count = True
            else:
                print(f'Sorry, {self.player_count} is not valid.')
        self.find_available_boards(board_details)
        valid_board = False
        while valid_board is False:
            self.current_board = input('Player X, select a board to play on: ').upper().strip()
            if self.current_board not in self.available_boards:
                print(f"Sorry, {self.current_board} isn't a valid board. Valid boards are {', '.join(self.available_boards)}")
            else:
                valid_board = True

    def find_available_boards(self, board_details):
        self.available_boards = []
        for cur_board in board_details:
            if cur_board != 'Main':
                self.find_available_squares(board_details, cur_board)
                if len(self.available_squares) > 0:
                    self.available_boards.append(cur_board)

    def player_choice(self, board_details):
        print('')
        self.find_available_squares(board_details, self.current_board)
        self.current_board_available(board_details)
        valid_choice = False
        while valid_choice is False:
            if self.player_count == '1' and self.current_player == 'O':
                sleep(1.5)
                choice = self.computer_choice_square()
            else:
                choice = input(
                    f'Player {self.current_player}, Select a square in board {self.current_board}: ').upper().strip()
            if choice in self.available_squares:
                self.current_choice = choice
                return
            else:
                print(f'{choice} is not available or valid. Please select another square')
                print(f'Available squares are {", ".join(self.available_squares)}')

    def find_available_squares(self, board_details, cur_board):
        self.available_squares = []
        for cur_square in board_details[cur_board]['squares']:
            if board_details[cur_board]['squares'][cur_square]['winner'] == 'none':
                self.available_squares.append(cur_square)

    def current_board_available(self, board_details):
        if self.current_board not in self.available_boards:
            valid_choice = False
            while valid_choice is False:
                if self.player_count == '1' and self.current_player == 'O':
                    self.current_board = self.computer_choice_board()
                else:
                    self.current_board = input(
                        f'{self.current_board} is full. Player {self.current_player}, select another board to play on: ').upper()
                if self.current_board in self.available_boards:
                    valid_choice = True
        self.find_available_squares(board_details, self.current_board)

    def win_subboard_check(self, board_details):
        if board_details[self.current_board]['winner'] == 'none':  # ensures won boards do not get reassigned
            # Next for loop identifies all squares won by current player within the current board
            squares_won = []
            for cur_square in board_details[self.current_board]['squares']:
                if board_details[self.current_board]['squares'][cur_square]['winner'] == self.current_player:
                    squares_won.append(cur_square)
            # For Loop checks to see if squares_won contains any winning sequences
            for cur_sequence in self.winning_sequences:
                win_count = 0
                for square in squares_won:
                    if square in cur_sequence:
                        win_count += 1
                if win_count >= 3:
                    board_details[self.current_board]['winner'] = self.current_player
                    self.subboard_winning_sequence = cur_sequence
                    self.win_in_round = True
                    return

    def win_mainboard_check(self, board_details):
        # Loop identifies all boards won by current player
        squares_won = []
        for cur_square in board_details:
            if board_details[cur_square]['winner'] == self.current_player:
                squares_won.append(cur_square)
        # For Loop checks to see if squares_won contains any winning sequences
        for cur_sequence in self.winning_sequences:
            win_count = 0
            for square in squares_won:
                if square in cur_sequence:
                    win_count += 1
            if win_count >= 3:
                board_details['Main']['winner'] = self.current_player
                self.mainboard_winning_sequence = cur_sequence
                self.game_over = True
                print(f'Congratulations Player {self.current_player}! You Won!')
                return

    def draw_game(self, board_details):
        available_boards = 0
        for cur_board in board_details:
            if cur_board != 'Main':
                self.find_available_squares(board_details, cur_board)
                if len(self.available_squares) > 0:
                    available_boards += 1
        if available_boards == 0:
            self.game_over = True
            print("It's a draw")

    def next_turn(self, choice):
        self.prior_board = self.current_board
        self.prior_choice = self.current_choice
        self.current_board = choice
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    # Logic for vs Computer Games
    def computer_choice_square(self):
        choice = random.choice(self.available_squares)
        print(f'Computer chooses square {choice} in board {self.current_board}')
        return choice

    def computer_choice_board(self):
        new_board = random.choice(self.available_boards)
        print(f'{self.current_board} is full. Computure chooses board {new_board}')
        return new_board
