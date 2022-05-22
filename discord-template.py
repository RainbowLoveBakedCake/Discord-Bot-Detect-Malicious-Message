#bot template from https://realpython.com/how-to-make-a-discord-bot-python/
import os
import discord
from dotenv import load_dotenv

#masukin tokennya
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

#connect client
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
client.run(TOKEN)