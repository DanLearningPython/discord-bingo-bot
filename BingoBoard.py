from PIL import Image,ImageDraw,ImageFont
import textwrap
from random import randint


class BingoBoard:

  def __init__(self, bingo_board):
    self.bingo_board = bingo_board

  def generate_board_image(self, file_name = 'bingo'):

    yPosition = 450
    cellWidth = 265
    cellHeight = 260
    margin = 10
    font = ImageFont.truetype("fonts/comic-sans.ttf", 28, encoding="unic")
    canvas = Image.open("bingo_template.png")
    draw = ImageDraw.Draw(canvas)

    for row in self.bingo_board:
      xPosition = 100
      for cell in row:
        text = textwrap.fill(cell[0], 13)
        draw.text((xPosition, yPosition), text, 'blue', font)
        xPosition += cellWidth
      yPosition += cellHeight

    rand_file_int = randint(0, 1333337);
    file_name = 'bingo_boards/' + file_name + '_' + str(rand_file_int) + '.png'
    canvas.save(file_name, "PNG")

    return file_name
