import click
import json
from gazpacho import get, Soup
source = click.prompt('Source valid address@')
BASE = source
titres = []
resumes = []
counter = 1
articles = []

def parse(page):
    result = {}
    titre = page.find('h2').find('a').text
    resume_temp = page.find('p').text
    result.update(titres=titre, resumes=resume_temp)
    articles.append(result)
    return None

for i in range(3):
    if counter == 1:
        url = BASE + "/page/" + str(counter)
    else:
        url = BASE + "/page/" + str(counter)
    counter += 1
    html = get(url)
    soup = Soup(html)
    entries = soup.find('div', {'class': 'archive-text'}, strict=False)
    for article in entries:
        parse(article)
    with open('data{}.json'.format(counter), 'w+', encoding='utf8') as outfile:
        json.dump(articles, outfile)
    articles = []
