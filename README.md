A Discord bot that generates randomized bingo board images

Copy config.dist.py and rename it to config.py. Place your token inside the file.

python WoWBingoBot.py

To generate test bingo board images locally, type:

python BingoTest.py


### Docker
`docker build -t bingobot .`

`docker run --rm -v $(pwd)/bingo_boards:/opt/bingobot/bingo_boards bingobot`
