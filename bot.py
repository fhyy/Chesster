import discord
import ids

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

client.run(clientKey)