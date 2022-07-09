import re

def parsing_message(message):
    for line in message:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        #print(urls)
    new_url = ''
    new_url += urls[0]
    return new_url
    

message = open("tutorial-for-learning-purposes\example.txt","r")
print(parsing_message(message))

