from player import Player, HumanPlayer, RandomComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # slicing array like 0:3,3:6,6:9
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # WE CAN DO BELOW ------------------
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot==' ':
        #         moves.append(i)
        # return moves

        # OR-------------------------
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_index = square % 3
        column = [self.board[i*3 + col_index] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        """
        GIVEN -> BOARD = [0,1,2,3,4,5,6,7,8] converted to below
        [0,1,2]
        [3,4,5]
        [6,7,8]
        
        WE CAN SEE THE DIAGONALS ARE 0,4,8 AND 2,4,6 and both these are divisible by 2
        
        """

        if square % 2 == 0:
            diagonal1 = [self.board[i]
                         for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # right to left diagonal

            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game: TicTacToe, x_player, o_player, print_game: bool = True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while len(game.available_moves()) > 0:
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if type(x_player) == RandomComputerPlayer and letter == 'X':
            print("****** THINKING ********")
            time.sleep(2)
            print("**** MAKING A MOVE *****")
            time.sleep(0.5)

        elif type(o_player) == RandomComputerPlayer and letter == 'O':
            print("****** THINKING ********")
            time.sleep(2)
            print("**** MAKING A MOVE *****")
            time.sleep(0.5)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " Wins!")
                return letter

            # this is a ternary operator like some_condition ? True : False similarly VALUE_IF_TRUE  if some_condition else VALUE_IF_FALSE
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It\'s a tie!")


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)  # you can set print
