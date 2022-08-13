import re
from urllib.parse import urlparse


def find_domain(url):
    domain = urlparse(url).netloc
    if domain.startswith('www.'):
        domain = re.sub(r'www.','',domain)
    return domain

print(find_domain("https://www.discord-login.ru/discord/"))








