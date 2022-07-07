##this code source from https://www.tutorialspoint.com/python_text_processing/python_extract_url_from_text.htm
import re
with open("tutorial-for-learning-purposes\example.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)