from urllib import response
import requests
import json
import base64
import re
from urllib.parse import urlparse

def api_scanurl(message):
    target_url = message
    if target_url.find('www'):
        target_url = re.sub(r'www.','',target_url)
        
        #uncomment below for debugging purpose only
        #print("target url", target_url)

    url_id = base64.urlsafe_b64encode(target_url.encode()).decode().strip("=")
    url = "https://www.virustotal.com/api/v3/urls/" + url_id

    # Api Key from your api virustotal account
    headers = {
        "Accept" : "application/json",
        "x-apikey" : "f873095544f7cb5a7be799220cb17e21b332f21578eed4d23d952a45e196074f"
    }

    response = requests.request("GET", url, headers=headers)
    decodedResponse = json.loads(response.text)
    
    #uncomment below for debugging purpose only
    #print(decodedResponse)

    malicious_score = (decodedResponse["data"]["attributes"]["last_analysis_stats"]["malicious"])
    return malicious_score

    ##test case to check malicious score
    # if malicious_score > 0 :
    #     print(malicious_score, 'Malicious URL')
    # else:
    #     print('URL Safe')

#test case
#print(api_scanurl("https://www.discord-login.ru/discord"))
