from bs4 import BeautifulSoup
import requests

def run_scraper():
    # Parse and collect page
    r = requests.get("https://us.battle.net/forums/en/sc2/40568/")
    soup = BeautifulSoup(r.content, "html.parser")
    for title in soup.find_all("span", class_="ForumTopic-title"):
        if ('Community Update' in title.text):
            for link in title.find_parents("a"):
                foundLink = requests.get("https://us.battle.net" + link.get("href"))
                soup = BeautifulSoup(foundLink.content, "html.parser")

                for authorCheck in soup.find_all("span", class_="Author-name"):
                    if ('Balance Team' in authorCheck.text):
                        with open("balanceChanges.txt", "w") as balanceChanges:
                            for content in soup.find("div", class_="TopicPost-bodyContent"):
                                balanceChanges.write(str(content) + "\n")


def removeWebTags():
    with open('balanceChanges.txt', 'r') as readFile:
        data = readFile.read()

        data = data.replace('<br/>', '\n')
        data = data.replace('<strong>', '**')
        data = data.replace('</strong>', '**')

    with open('balanceChanges.txt', 'w') as file:
            file.write(data)
