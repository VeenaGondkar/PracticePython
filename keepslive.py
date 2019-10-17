
from urllib.request import urlopen
import re

#connect to a URL
website = urlopen("https://www.google.com/")

#read html code
html = website.read()

# use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', str(html))

for i in links:
    print(i[0])
