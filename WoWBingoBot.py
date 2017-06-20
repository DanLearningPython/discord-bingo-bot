import discord
from WowBingo import WowBingo
import config

client = discord.Client()
bingo = WowBingo()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = message.content.split()[0]

    handler = {
        "?bingo": bingo_handler,
        "?about": about_handler
    }.get(command, noop_handler)

    await handler(message)

    return

async def bingo_handler(message):
    msg = 'Hello {0.author.mention}'.format(message)

    if message.author.name == 'LinaeSostra' :
        msg = 'Here\'s your bingo card you trash panda {0.author.mention}'.format(message)
    elif message.author.name == 'Netflixnheal':
        msg = 'Here you go master: '

    await client.send_message(message.channel, msg)
    await client.send_file(message.channel, bingo.generate_board(message.author.name))

    return

async def about_handler(message):
    msg = 'Bingo bot for dank memes...by Dan'
    await client.send_message(message.channel, msg)

    return

async def noop_handler(message):
    pass

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.auth['token'])
