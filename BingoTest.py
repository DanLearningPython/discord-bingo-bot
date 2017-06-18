from WowBingo import WowBingo

bingo = WowBingo()
file_name = bingo.generate_board('dan')
print("Generated bingo board: " + file_name)
