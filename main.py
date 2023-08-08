class ConnectFour:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.player_turn = 'X'
        self.game_over = False

    def print_board(self):
        print()
        for row in self.board:
            print(' | '.join(row))
            print('--' * (len(row) * 2 - 1))

    def is_valid_move(self, col):
        return self.board[0][col] == ' '

    def make_move(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.player_turn
                break

    def check_winner(self):
        def check_direction(dx, dy):
            for row in range(self.rows):
                for col in range(self.cols):
                    if (
                        0 <= row + 3 * dx < self.rows and
                        0 <= col + 3 * dy < self.cols
                    ):
                        if all(
                            self.board[row + i * dx][col + i * dy] == self.player_turn
                            for i in range(4)
                        ):
                            return True
            return False

        return (
            check_direction(1, 0) or
            check_direction(0, 1) or
            check_direction(1, 1) or
            check_direction(1, -1)
        )

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def play(self):
        while not self.game_over:
            self.print_board()
            col = int(input(f"Player {self.player_turn}, choose a column (0-{self.cols - 1}): "))

            if col < 0 or col >= self.cols:
                print("Invalid column. Please choose a valid column.")
                continue

            if not self.is_valid_move(col):
                print("Column is already full. Choose another column.")
                continue

            self.make_move(col)

            if self.check_winner():
                self.print_board()
                print(f"Player {self.player_turn} wins!")
                self.game_over = True

            if self.is_full():
                self.print_board()
                print("It's a draw!")
                self.game_over = True

            self.player_turn = 'O' if self.player_turn == 'X' else 'X'


if __name__ == "__main__":
    game = ConnectFour()
    game.play()