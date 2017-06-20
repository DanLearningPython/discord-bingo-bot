import random
import csv
from BingoBoard import BingoBoard


class WowBingo:

    def __init__(self, grid_size = 5, file_name = 'cards.txt'):
        self.grid_size = grid_size
        self.bingo_options = self._read_file(file_name)

    def _read_file(self, file_name):
        bingo_file = open(file_name, 'rt', encoding="utf8")
        reader = csv.reader(bingo_file)
        bingo_options = list(reader)
        return bingo_options

    def generate_board(self, user_name):
        board_layout = self.generate_board_layout()
        bingo_board = BingoBoard(board_layout)
        board_image = bingo_board.generate_board_image(user_name=user_name)

        return board_image

    def generate_board_layout(self):
        randRange = range(0,len(self.bingo_options))
        option_pool = random.sample(randRange, self.grid_size * self.grid_size)

        board = []
        row = []

        for option in option_pool:
            if len(row) == self.grid_size:
                board.append(row)
                row = []
            row.append(self.bingo_options[option])
        board.append(row)

        return board
