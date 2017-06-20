from PIL import Image,ImageDraw,ImageFont
import textwrap
from random import randint


class BingoBoard:

    def __init__(self, bingo_board):
        self.bingo_board = bingo_board

    def generate_board_image(self, file_name='bingo', user_name='anon'):

        y_position = 450
        cell_width = 265
        cell_height = 260
        margin = 10
        font = ImageFont.truetype("fonts/ComicRelief-Bold.ttf", 28, encoding="unic")
        canvas = Image.open("bingo_template.png")
        draw = ImageDraw.Draw(canvas)

        for row in self.bingo_board:
            x_position = 100
            for cell in row:
                text = textwrap.fill(cell[0], 13)
                draw.text((x_position, y_position), text, 'blue', font)
                x_position += cell_width
            y_position += cell_height

        rand_file_int = randint(0, 1333337);
        file_name = 'bingo_boards/' + file_name + '_' + user_name + '_' + str(rand_file_int) + '.png'
        canvas.save(file_name, "PNG")

        return file_name
