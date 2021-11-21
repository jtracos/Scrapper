import requests
from lxml import html
import xpath
from datetime import datetime
import os
class scrapper:

    def __init__(self,url):
        self.url = url


    def parse_note(self, date):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                if not os.path.isdir(date):
                    os.mkdir(date)

                text = response.content.decode("utf-8")
                parsed_note = html.fromstring(text)
                body = parsed_note.xpath(xpath.CORPUS)
                title = parsed_note.xpath(xpath.TITLE_CORPUS)[0].replace("¿","").replace("?","").\
                    replace("¡","").replace("!","")
                with open(f"./{date}/{title}.txt", mode="w") as f:
                    f.write(title.upper())
                    f.write("\n\n")
                    for line in body:
                        f.write(line)
                        f.write("\n")

            else:
                raise ValueError(f"Codigo de error: {response.status_code}")
        except ValueError as ve:
            print(ve)


    def parse_home(self):
        try:
            response = requests.get(xpath.TH)
            if response.status_code == 200:
                home = response.content.decode("utf-8")
                parsed = html.fromstring(home)
                links = parsed.xpath(xpath.LINKS)
                DATE_STR = datetime.today().strftime("%d-%m-%Y")
                for link in links:
                    self.parse_note(link, DATE_STR)
            else:
                raise ValueError(f"Error: {response.status_code}")
        except ValueError as ve:
            print(ve)
    

    def __call__(self,):
        self.parse_home()


if __name__ == "__main__":

    scrapper(xpath.TH)()
