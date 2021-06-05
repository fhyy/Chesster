import discord
import ids
import chess as chs
import assets as ass
import visualizer as viz
import random
import base64

intents = discord.Intents(messages=True, members=True, guilds=True)
client = discord.Client(intents=intents)

channelIds = ids.channelIds
clientKey = ids.clientKey

nextGameCounter = 99999999999

finishedGames = []
ongoingGames = []
gameAwaitingPlayers = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channelId = message.channel.id
    if message.author == client.user or channelId not in channelIds:
        return

    if message.content == "Hey Chesster":
        await client.get_channel(channelId).send("Hello, <@"+str(message.author.id)+">!")
    
    if message.content == "new game":
        await client.get_channel(channelId).send(resetBoard())
        
    if message.content == "Print board":
        await client.get_channel(channelId).send(viz.getBoardString(chs.startingBoardState()))

    if message.content == "Game ID":
        await client.get_channel(channelId).send(getNextGameId())
        
def getNextGameId():
    global nextGameCounter
    nextGameCounter = nextGameCounter - random.randint(1,10)
    return base64.b32encode(nextGameCounter.to_bytes(5, byteorder='little'))[:4].decode("utf-8")

### TODO: Syntax
# > Play white      -- Author queues up for a game playing White. Starts game if Black player awaiting White opponent
# > Play black      -- Author queues up for a game playing Black. Starts game if White player awaiting Black opponent
# > Play <color> AI -- Author queues up for a game playing <color> vs the AI.
# > A3              -- Author makes a move to A3 from the if there's only one valid move to A3, and it's their turn in one game.
# > A2-A3           -- Author makes a move from A1 to A2, if valid, and it's their turn in one game.
# > 6XEZ: A3        -- Author makes a move from A1 to A2 in game 6XEZ if there's only one valid move to A3.
# > 6XEZ: A2-A3     -- Author makes a move from A1 to A2 in game 6XEZ, if valid.
#
### Grammar:
# > Play <COLOR>{ AI}?
# > {<GAME_ID>: }?{<FROM_POS>-}?<TO_POS>
###

client.run(clientKey)
