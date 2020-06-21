import re
import json
from gazpacho import get, Soup
from html.parser import HTMLParser
from html.entities import name2codepoint

url = 'http://www.fdesouche.com/category/securite'
html = get(url)
soup = Soup(html)
entries = soup.find('div', {'class': 'archive-text'}, strict=False)
articles = []
titres = []
resumes = []

def parse(art):
    result = {}
    titre = art.find('h2').find('a').text
    resume_temp = art.find('p').text
    result.update( titres = titre, resumes =resume_temp)
    articles.append(result)
    return None

[parse(article) for article in entries]

# for a in articles:
    # print(a)
    # print("\n")

with open('data.txt', 'w+') as outfile:
    json.dump(articles, outfile)


