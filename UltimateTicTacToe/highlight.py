from turtle import Turtle


class Highlight(Turtle):
    def __init__(self, screen_size):
        super().__init__()
        self.hideturtle()
        self.boardsize = screen_size / 3 * .85
        self.squaresize = screen_size / 9 * .9
        self.speed(10)
        self.pensize(5)

    def highlight_board(self, current_player, current_board, board_details):
        self.clear()
        self.penup()
        x_start = board_details[current_board]['xcor'] - self.boardsize / 2
        y_start = board_details[current_board]['ycor'] - self.boardsize / 2
        self.setposition(x_start, y_start)
        self.pendown()
        if current_player == 'X':
            self.color('blue')
        else:
            self.color('red')
        for n in range(0, 4):
            self.forward(self.boardsize)
            self.left(90)

    def highlight_square(self, current_player, prior_board, prior_choice, board_details):
        # self.clear()
        self.penup()
        x_start = board_details[prior_board]['squares'][prior_choice]['xcor'] - self.squaresize / 2
        y_start = board_details[prior_board]['squares'][prior_choice]['ycor'] - self.squaresize / 2
        self.setposition(x_start, y_start)
        self.pendown()
        # color logic is backwards as this square is for the previous player
        if current_player == 'X':
            self.color('red')
        else:
            self.color('blue')
        for n in range(0, 4):
            self.forward(self.squaresize)
            self.left(90)
