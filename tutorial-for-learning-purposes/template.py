##this is for testing purposes only

from urllib import response
import discord
import random

#token is from Discord Developer Portal > Bot > you will generate token, just copy and put it here
TOKEN = 'DISCORD-API-KEY'
client = discord.Client()

#turn on your discord bot
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')

     # To make the bot don't read message from it's own
    if message.author == client.user:
        return
    
    #name of channel
    if message.channel.name == 'testing-command':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(10000000)}'
            await message.channel.send(response)
            return
    
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return

client.run(TOKEN)
