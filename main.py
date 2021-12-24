import argparse
import yaml
import datetime
from common import config, save, __config, current_date, set_name
from lxml import html
import logging
import csv
from scrapper import *
#logging.getLevelName(logging.INFO)
logging.basicConfig()
logger = logging.getLogger(__name__)


def scrapper(site):
    import requests
    logging.warning("starting job {}".format(site))

    home = Home(site)
    home.parse()

    p = f"./data/{site}_{current_date}.csv"
    article = Article(site)
    with open(p, mode="w") as file:
        writer = csv.writer(file, quotechar='"')
        fieldnames = [attr for attr in dir(article) if attr not in dir(home)+["set_path", "_path"]]
        writer.writerow(fieldnames)
        logging.info(f"obtaining {fieldnames}")
        for link in home.links:
            article.set_path(link)
            article.parse()
            logging.warning(fr"Extracting data from {article.url}")
            fields = [getattr(article, attr) for attr in dir(article) if attr not in dir(home)+["set_path", "_path"]]

            writer.writerow(fields)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_site_choices = list(config()['sites'].keys())
    now = datetime.datetime.now()
    parser.add_argument('sites',
                        help='Sitio del que desea minar las noticias',
                        type=str,
                        choices=new_site_choices)

    args = parser.parse_args()
    scrapper(args.sites)
    logging.warning("Tiempo total empleado {}".format(datetime.datetime.now() - now))
