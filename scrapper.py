import requests
from lxml import html
import xpath
from datetime import datetime
import os
class scrapper:

    def __init__(self,url):
        self.url = url


    def parse_note(self, link, current_date):
        try:
            link = self.url + link
            
            response = requests.get(link)
            if response.status_code == 200:
                diario = self.url.replace("www.","").lower().replace("https://","").replace(".","-")
                home = response.content.decode("utf-8")
                parsed_home = html.fromstring(home)
                date = parsed_home.xpath(xpath.AR_DATE)[0].replace("/","-")
                print(date)
                body = parsed_home.xpath(xpath.AR_BODY)
                resumen = parsed_home.xpath(xpath.AR_RESUMEE)
                title = parsed_home.xpath(xpath.AR_TITLE)[0].replace("¿","").replace("?","").\
                    replace("¡","").replace("!","").strip().replace(".","_").replace(" ","-")
                    #entradas para fecha corriente y fecha de la nota
                p = f"./{diario}/{current_date}/{date}"
                if not os.path.isdir(p):
                    os.makedirs(p)

                with open(p + f"/{title}.txt", mode="w") as f:
                    f.write(title.upper())
                    f.write("\n" + date)
                    f.write("\n\n")
                    for line in resumen:
                        f.write(line)
                        f.write("\n")
                    for line in body:
                        f.write(line)
                        f.write("\n")

            else:
                raise ValueError(f"Codigo de error: {response.status_code}")
        except ValueError as ve:
            print(ve)


    def main(self):
        try:
            response = requests.get(xpath.DP)
            if response.status_code == 200:
                home = response.content.decode("utf-8")
                parsed = html.fromstring(home)
                links= parsed.xpath(xpath.DP_LINKS)
                DATE_STR = datetime.today().strftime("%d-%m-%Y")
                for link in links:
                    self.parse_note(link, DATE_STR)
            else:
                raise ValueError(f"Error: {response.status_code}")
        except ValueError as ve:
            print(ve)
    

    def __call__(self,):
        self.main()


if __name__ == "__main__":

    scrapper(xpath.DP)()
