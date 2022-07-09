#tutorial 1 : https://realpython.com/how-to-make-a-discord-bot-python/
#tutorial 2 : https://www.youtube.com/watch?v=fU-kWx-OYvE

from urllib import response
import discord
import re
from joblib import Parallel, delayed
import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np
from api_called import API


#parsing message
def parsing_message(message):
    for line in message:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        #print(urls)
    new_url = ''
    new_url += urls[0]
    return new_url

#connect to machine learning
def machine_learning_function(parsed_message):
    parsed_message = [[parsed_message]]
    labelEncoder = LabelEncoder()
    # reshape data string to float something
    parsed_message = labelEncoder.fit_transform(parsed_message)
    parsed_message = np.reshape(parsed_message, (1, -1))
    
    # Load the model from the file
    ml_model = joblib.load('machine_learning\ml_model.pkl')
 
    # Use the loaded model to make predictions
    prediction = ml_model.predict(parsed_message)
    #print(prediction)
    result = prediction[0]
    return prediction

#connect to api virus total
def api_vt_function(parsed_message):
    detect_url = API.api_scanurl(parsed_message)
    return detect_url

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
        #await client.send_message()
        await message.channel.send()

        #parsing 
        parsed_message = parsing_message(client.user_message)
        url_detect_beginning = machine_learning_function(parsed_message)
        if url_detect_beginning == 1:
            #checking again with virus total
            url_detect_final = api_vt_function(parsed_message)
            if url_detect_final > 0:
                #delete message
                await message.delete()


client.run(TOKEN)