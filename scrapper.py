import requests
from lxml import html
import autopep8
import xpath

def parse():
    try:
        response = requests.get(xpath.TH)
        if response.status_code == 200:
            home = response.content.decode("utf-8")
            parsed = html.fromstring(home)
            links = parsed.xpath(xpath.LINKS)
            for link in links:
                print(links)
        else:
            raise ValueError(f"Error: {response.status_code}")
    except ValueError as ve:
        print(ve)

def run():
    parse()

if __name__ == "__main__":

    run()
