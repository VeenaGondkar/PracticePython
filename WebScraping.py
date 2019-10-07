from lxml import html
import requests

page = requests.get('https://www.guru99.com/software-testing.html')
tree = html.fromstring(page.content)

for i in range(1,18):
    for j in range(1,25):
        titles = tree.xpath('//table[' + str(i) + ']/tr[' + str(j) + ']/td[2]/text()')
        if titles != []:
            print(titles[0])