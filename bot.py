import discord
import ids
import setup
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

client.run(clientKey)
