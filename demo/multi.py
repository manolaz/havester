import click
import json
from gazpacho import get, Soup
source = click.prompt('Source valid address@ pour Les Observateurs.ch/')
limit = int(click.prompt('NUMBER of PAGES to havest'))
BASE = source
titres = []
resumes = []
counter = 1
articles = []

def parse(page):
    result = {}
    titre = page.find('h3',{'class': 'entry-title'}, strict=False).find('a').text
    resume_temp = page.find('div', {'class': 'entry-content'}, strict=False).find('p').text
    pubdate = page.find('time', {'class': 'entry-date'}, strict=False).find('a').text
    result.update(titre=titre, resume=resume_temp, date = pubdate)
    articles.append(result)
    return None

for i in range(limit):
    if counter == 1:
        url = BASE + "page/" + str(counter)
    else:
        url = BASE + "page/" + str(counter) + "/"
    counter += 1
    html = get(url)
    soup = Soup(html)
    entries = soup.find('article', {'class': 'archive-entry'}, strict=False)
    for article in entries:
        parse(article)
    with open('data{}.json'.format(counter-1), 'w+', encoding='utf-8') as outfile:
        json.dump(articles, outfile)
    articles = []
