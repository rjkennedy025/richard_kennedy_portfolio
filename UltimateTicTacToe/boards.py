from turtle import Turtle

SIZE_1 = 900
SIZE_2 = SIZE_1 / 3 * .75
# X_SEQUENCE and Y_SEQUENCE used to set starting point for lines in each board
X_SEQUENCE = [-1 / 6, 1 / 6, -1 / 2, -1 / 2]
Y_SEQEUNCE = [1 / 2, 1 / 2, 1 / 6, -1 / 6]
HEADING_SEQUENCE = [270, 270, 0, 0]
POS_A = 1 / 3 * -1
POS_B = 0
POS_C = 1 / 3
POS_1 = 1 / 3
POS_2 = 0
POS_3 = 1 / 3 * -1


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(10)
        # self.board_details = BOARD_DETAILS
        self.board_details = []
        self.set_board_details()
        self.screen_size = SIZE_1

    def set_board_details(self):
        self.board_details = {'Main': {'xcor': SIZE_1 * 0, 'ycor': SIZE_1 * 0, 'winner': 'none'},
                              'A1': {'xcor': SIZE_1 * POS_A, 'ycor': SIZE_1 * POS_1, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'A2': {'xcor': SIZE_1 * POS_A, 'ycor': SIZE_1 * POS_2, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'A3': {'xcor': SIZE_1 * POS_A, 'ycor': SIZE_1 * POS_3, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_A + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'B1': {'xcor': SIZE_1 * POS_B, 'ycor': SIZE_1 * POS_1, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'B2': {'xcor': SIZE_1 * POS_B, 'ycor': SIZE_1 * POS_2, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'B3': {'xcor': SIZE_1 * POS_B, 'ycor': SIZE_1 * POS_3, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_B + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'C1': {'xcor': SIZE_1 * POS_C, 'ycor': SIZE_1 * POS_1, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_1 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'C2': {'xcor': SIZE_1 * POS_C, 'ycor': SIZE_1 * POS_2, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_2 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              'C3': {'xcor': SIZE_1 * POS_C, 'ycor': SIZE_1 * POS_3, 'winner': 'none', 'squares': {
                                  'A1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'A2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'A3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_A,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'B1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'B2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'B3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_B,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'},
                                  'C1': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_1,
                                         'winner': 'none'},
                                  'C2': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_2,
                                         'winner': 'none'},
                                  'C3': {'xcor': SIZE_1 * POS_C + SIZE_2 * POS_C,
                                         'ycor': SIZE_1 * POS_3 + SIZE_2 * POS_3,
                                         'winner': 'none'}
                              }},
                              }

    def create_board(self):
        for cur_board in self.board_details:
            self.color('black')
            if cur_board == 'Main':
                self.pensize(10)
                size = SIZE_1
            else:
                self.pensize(5)
                size = SIZE_2
            xcenter = self.board_details[cur_board]['xcor']
            ycenter = self.board_details[cur_board]['ycor']
            for n in range(0, 4):
                self.penup()
                self.setposition(x=size * X_SEQUENCE[n] + xcenter, y=size * Y_SEQEUNCE[n] + ycenter)
                self.setheading(HEADING_SEQUENCE[n])
                self.pendown()
                self.forward(size)
                self.penup()
            # for square in curboard write square name
            if cur_board != 'Main':
                label_size = int(SIZE_2 * .04)
                self.color('grey')
                for cur_square in self.board_details[cur_board]['squares']:
                    label_x = self.board_details[cur_board]['squares'][cur_square]['xcor']
                    label_y = self.board_details[cur_board]['squares'][cur_square]['ycor'] - label_size / 2
                    self.setposition(label_x, label_y)
                    self.write(arg=cur_square, move=False, align='center', font=("Arial", label_size, "normal"))
        self.grid_headers()

    def grid_headers(self):
        print_order = ['A', 'B', 'C', '1', '2', '3']
        self.color('black')
        font_size = int(.05) * SIZE_1
        x_order = [SIZE_1 * POS_A, SIZE_1 * POS_B, SIZE_1 * POS_C, -SIZE_1 * .52, -SIZE_1 * .52, -SIZE_1 * .52]
        y_order = [SIZE_1 * .48, SIZE_1 * .48, SIZE_1 * .48, SIZE_1 * POS_1, SIZE_1 * POS_2, SIZE_1 * POS_3]
        for n in range(0, 6):
            if n <= 2:
                x_adjust = font_size / 3
                y_adjust = 0
            else:
                x_adjust = 0
                y_adjust = font_size / 2
            self.setposition(x_order[n] - x_adjust, y_order[n] - y_adjust)
            self.write(arg=print_order[n], move=False, font=('Arial', font_size, 'bold'))

    def place_marker(self, current_player, current_board, choice):
        xcenter = self.board_details[current_board]['squares'][choice]['xcor']
        ycenter = self.board_details[current_board]['squares'][choice]['ycor']
        self.setposition(xcenter, ycenter)
        if current_player == 'X':
            self.pendown()
            self.color('blue')
            for heading in (45, 135, 225, 315):
                self.setposition(xcenter, ycenter)
                self.setheading(heading)
                self.forward(25)
        else:
            self.color('red')
            self.sety(ycenter - 20)
            self.setheading(0)
            self.pendown()
            self.circle(20)
        self.penup()
        self.board_details[current_board]['squares'][choice]['winner'] = current_player

    def subboard_winning_line(self, current_player, current_board, winning_sequence):
        if current_player == 'X':
            self.color('blue')
        else:
            self.color('red')
        x_start = self.board_details[current_board]['squares'][winning_sequence[0]]['xcor']
        y_start = self.board_details[current_board]['squares'][winning_sequence[0]]['ycor']
        x_end = self.board_details[current_board]['squares'][winning_sequence[2]]['xcor']
        y_end = self.board_details[current_board]['squares'][winning_sequence[2]]['ycor']
        self.setposition(x_start, y_start)
        self.pendown()
        self.setposition(x_end, y_end)
        self.penup()

    def mainboard_winning_line(self, current_player, winning_sequence):
        self.pensize(10)
        if current_player == 'X':
            self.color('blue')
        else:
            self.color('red')
        x_start = self.board_details[winning_sequence[0]]['xcor']
        y_start = self.board_details[winning_sequence[0]]['ycor']
        x_end = self.board_details[winning_sequence[2]]['xcor']
        y_end = self.board_details[winning_sequence[2]]['ycor']
        self.setposition(x_start, y_start)
        self.pendown()
        self.setposition(x_end, y_end)
        self.penup()
