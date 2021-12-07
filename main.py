import argparse
import yaml
import os
from common import config, save, __config, current_date, set_name
from lxml import html
import logging
import os
from scrapper import *

logger = logging.getLogger(__name__)


def scrapper(site):
    import requests
    logging.warning("comenzando minado en {}".format(site))

    home = Home(site)
    home.parse()
    article = Article(site)
    for link in home.links:
        article.set_path(link)
        article.parse()
        date = article.date.replace("/","-")
        p = f"./{'diariopresente'}/{current_date}/{date}"
        print(article.title)
        save(p, set_name(article.title), article.title, article.resumen, article.body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_site_choices = list(config()['sites'].keys())
    parser.add_argument('sites',
                        help='Sitio del que desea minar las noticias',
                        type=str,
                        choices=new_site_choices)

    args = parser.parse_args()
    scrapper(args.sites)
