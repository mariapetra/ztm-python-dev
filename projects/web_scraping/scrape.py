import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

links = soup.select(".titleline > a")
subtext = soup.select(".subtext")
links2 = soup2.select(".titleline > a")
subtext2 = soup2.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))


# can add .select:
# votes = soup.select(".score").select
# https://docs.python.org/3/library/pprint.html
# print(soup)
# beautiful soup - allows you to parse - covert all your html data from a str to html you can use
# we need to do this because it also can use different parsers eg xml
# print(soup.body)
# print(soup.find_all("a"))
# can target certain parts of the html
# or find all of a certain type eg attributes
# why do this? because we want certain parts of the website


# select lets you grab a piece if data using the css selector
# - select a class/id or other css selector:
# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
