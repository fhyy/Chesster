import discord
import ids
import setup
import assets as ass

intents = discord.Intents(messages=True, members=True, guilds=True)
client = discord.Client(intents=intents)

channelId = ids.channelId
clientKey = ids.clientKey

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.channel.id != channelId:
        return

    if message.content == "Hey Chesster":
        await client.get_channel(channelId).send("Hello, <@"+str(message.author.id)+">!")
    
    if message.content == "new game":
        await client.get_channel(channelId).send(resetBoard())
        
    if message.content == "Print board":
        await client.get_channel(channelId).send(getBoardInUglyManner())

def getBoardInUglyManner():
    return (
        "```prolog"
        "8"+ " "+ass.blackRook + " "+ass.blackKnight + " "+ass.blackBishop + " "+ass.blackQueen + " "+ass.blackKing + " "+ass.blackBishop + " "+ass.blackKing + " "+ass.blackRook + '\n'
        "7"+ " "+ass.blackPawn + " "+ass.blackPawn + " "+ass.blackPawn + " "+ass.blackPawn + " "+ass.blackPawn + " "+ass.blackPawn + " "+ass.blackPawn + " "+ass.blackPawn + '\n'
        "6"+ " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + '\n'
        "5"+ " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + '\n'
        "4"+ " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + '\n'
        "3"+ " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + " "+ass.blackSquare + " "+ass.whiteSquare + '\n'
        "2"+ " "+ass.whitePawn + " "+ass.whitePawn + " "+ass.whitePawn + " "+ass.whitePawn + " "+ass.whitePawn + " "+ass.whitePawn + " "+ass.whitePawn + " "+ass.whitePawn + '\n'
        "1"+ " "+ass.whiteRook + " "+ass.whiteKnight + " "+ass.whiteBishop + " "+ass.whiteQueen + " "+ass.whiteKing + " "+ass.whiteBishop + " "+ass.whiteKing + " "+ass.whiteRook + '\n'
        ". A B C D E F G H"
        "```"
    )
        
client.run(clientKey)
