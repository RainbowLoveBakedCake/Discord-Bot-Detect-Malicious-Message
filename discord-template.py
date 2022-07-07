#bot template from https://realpython.com/how-to-make-a-discord-bot-python/
import os
import discord
from dotenv import load_dotenv

#masukin tokennya
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

#connect client
@client.event
async def on_ready():
#    for guild in client.guilds:
#        if guild.name == GUILD:
#            break
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n -'.join([member.name for member in guild.members])
    printf(f'Guild Members:\n - {members}' )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my discord server!'
    )

@client.event
async def on_message(message):
    # Get username of the message sender
    username = str(message.author).split('#')[0]
    # Get the message content
    user_message = str(message.content)
    # Get the discord text channel where the messeges sent
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # To make the bot don't read message from it's own
    if message.author == client.user:
        return

client = CustomClient()
client.run(TOKEN)