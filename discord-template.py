import discord
import re
from urllib.parse import urlparse
import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np
from api_called import API

#taking domain-only from
def find_domain(url):
    domain = urlparse(url).netloc
    if domain.startswith('www.'):
        domain = re.sub(r'www.','',domain)
    return domain

#parsing message
def parsing_message(message):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', message)
    
    #uncomment below for debugging purposes only
    #print(urls)
    
    return urls

#connect to machine learning
def machine_learning_function(parsed_message):
    ml_parsed_message = parsed_message
    
    #uncomment below for debugging purposes only
    #print("ml_parsed_message: ", ml_parsed_message)
    
    #for taking domain-only to be checked by machine learning
    machinelearning_domain_only = ' '.join(map(str, ml_parsed_message))
    ml_final_predict = find_domain(machinelearning_domain_only)
    ml_final_predict = [ml_final_predict]
    
    #uncomment below for debugging purposes only
    #print("ml_final_predict : ", ml_final_predict)
    
    labelEncoder = LabelEncoder()
    
    # reshape data string to float something
    ml_parsed_message = labelEncoder.fit_transform(ml_parsed_message)
    ml_parsed_message = np.reshape(ml_parsed_message, (1, -1))
    
    # Load the model from the file
    # if using linux just uncomment line 49 and comment line 48
    ml_model = joblib.load('machine_learning\ml_model.pkl')
    # ml_model = joblib.load('machine_learning/ml_model.pkl')
 
    # Use the loaded model to make predictions
    prediction = ml_model.predict(ml_parsed_message)

    result = prediction[0]
    return result

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
    
    #if people send a new message -> just to make sure bot running in discord
    #while True:
        #await client.send_message()
    #await message.channel.send('checking ...')

    #parsing message -> array and detect with machine learning
    parsed_message = parsing_message(user_message)
    url_detect_beginning = machine_learning_function(parsed_message)
    
    
    #uncomment below for debugging purposes only
    #print("parsed_message: ", parsed_message)

    #because api just accept string 
    new_parsed_message = ' '.join(map(str, parsed_message))
    
    #uncomment below for debugging purposes only
    #print("new_parsed_message: ", new_parsed_message)
   
   #if machine learning detect this malicious
    if url_detect_beginning == 1:
        #checking again with virus total
        url_detect_final = api_vt_function(new_parsed_message)
        print("new_parsed_message: ", new_parsed_message)
        if url_detect_final + url_detect_beginning > 1:
            
            ##uncomment below for debugging this bot
            #print("user_message: ",user_message)
            #print("type of user_message:", type(user_message))
            #print("url detect beginning:",url_detect_beginning)
            #print("type of user_detect_beginning:", type(url_detect_beginning))
            #print("url detect final:",url_detect_final)
            #print("type of url_detect_final:", type(url_detect_final))
            
            #delete message
            await message.delete()
            await message.channel.send("Message from "+ str(message.author) +" has been deleted due to trying sending malicious messages")
            
#make sure bot running with token that already generated in discord developer portal
client.run(TOKEN)
