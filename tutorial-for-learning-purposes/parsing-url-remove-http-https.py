import re
#given_url = 'https://www.translate.google.com'

#print(re.sub('http?://www.','',given_url))
url = re.compile(r"https?://(www\.)?")
given_url = url.sub('', 'http://www.google.com/images').strip().strip('/')

print(given_url)
