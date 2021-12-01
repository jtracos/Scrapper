import requests
from lxml import html
import patterns
from datetime import datetime
import os
from common import *
import logging
import psycopg2

logger = logging.getLogger(__name__)
class Scrapper:

    def __init__(self, site):
        self._host = config()['sites'][site]['url']
        self.__site = site

    def parse_note(self, link, current_date):
        try:
            link = self._host + link

            response = requests.get(link)
            if response.status_code == 200:
                diario = self._host.replace("www.", "").lower().replace("https://", "").replace(".", "-")
                date = self.parse_page(response, config()["sites"][self.__site]["article"]["date"])[0].replace("/", "-")
                print(date)
                body = self.parse_page(response, config()["sites"][self.__site]["article"]["body"])
                resumen = self.parse_page(response, config()["sites"][self.__site]["article"]["resumen"])
                title = self.parse_page(response, config()["sites"][self.__site]["article"]["header"])[0]
                title_ = self.set_title(title)

                # entradas para fecha corriente y fecha de la nota
                p = f"./{diario}/{current_date}/{date}"
                if not os.path.isdir(p):
                    os.makedirs(p)
                
                with open(p + f"/{title_}.txt", mode="w") as f:
                    f.write(title.upper().strip())
                    # f.write("\n" + date)
                    f.write("\n")
                    for line in resumen:
                        f.write(line.strip().replace("\n", " "))
                        f.write("\n")
                    for line in body:
                        f.write(line)
                        f.write("\n")            

            else:
                raise ValueError(f"Codigo de error: {response.status_code}")
        except ValueError as ve:
            print(ve)


    def retrieve(self):
        try:
            response = requests.get(self._host)
            if response.status_code == 200:
                links = self.parse_page(response, patterns.DP_LINKS)
                date_str = datetime.today().strftime("%d-%m-%Y")
                for link in links:
                    self.parse_note(link, date_str)
            else:
                raise ValueError(f"Error: {response.status_code}")
        except ValueError as ve:
            print(ve)


    @staticmethod
    def parse_page(response, xpath):
        home = response.content.decode("utf-8")
        parsed = html.fromstring(home)
        return parsed.xpath(xpath)


    def set_title(self, title):
        import re
        match = re.findall("[a-zA-Z0-9\s]", title)
        
        return "".join(match).strip().replace(" ","-")






    





