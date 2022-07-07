#bot template from https://realpython.com/how-to-make-a-discord-bot-python/
#tutorial 2 : https://www.youtube.com/watch?v=fU-kWx-OYvE

from urllib import response
import discord
import re

#parsing message
def parsing_message(message):
    for line in message:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        #parsing again to remove http
        if urls
        return urls

#connect to machine learning
def machine_learning_function(message):
    return

#connect to api virus total
def api_vt_function(message):
    
    return 

#token is from Discord Developer Portal > Bot > you will generate token, just copy and put it here
TOKEN = 'OTg4MDYxNDcxODQ4MTQ0OTI2.Gmk0uu.pYSYTnONNCQFzPxtnSdKV2vWJ_Dp8qlDpylSKI'
client = discord.Client()

#turn on your discord bot
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

#reading the message
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')

     # To make the bot don't read message from it's own
    if message.author == client.user:
        return
    
    #if people send a new message 
    while True:
        await client.send_message()
        
        #parsing 
        parsed_message = parsing_message(client.user_message)
        url_detect_beginning = machine_learning_function(parsed_message)
        if url_detect_beginning == '':
            #delete message
            await message.delete()

            #checking again with virus total
            url_detect_final = api_vt_function(parsed_message)
            if url_detect_final > 0:
                #delete message
                await message.delete()

client.run(TOKEN)