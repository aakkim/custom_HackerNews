import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://news.ycombinator.com/news?p='

for page in range(1,5):
    response = requests.get(URL + str(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')


    def sort_stories_by_votes(hnlist):
        return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

    def create_custom_HN(links, subtext):
        hn = []
        for i, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None)
            vote = subtext[i].select('.score')
            if len(vote):
                likes = int(vote[0].getText().replace(' points', ' '))
                if likes > 99:
                    hn.append({'title': title, 'link': href, 'votes': likes})
        return sort_stories_by_votes(hn)

pprint.pprint(create_custom_HN(links, subtext))