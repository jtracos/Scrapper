import argparse
import yaml
import os
from common import config, save, __config
from lxml import html
import logging
import os
from scrapper import *

logger = logging.getLogger(__name__)


def scrapper(site):
    import requests
    logging.info("comenzando minado en {}".format(site))

    home = Home(site)
    article = Article(site)
    home.parse()
    
    for link in home.links:
        article.set_path(link)
        article.parse()
        print(article.title.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_site_choices = list(config()['sites'].keys())
    parser.add_argument('sites',
                        help='Sitio del que desea minar las noticias',
                        type=str,
                        choices=new_site_choices)

    args = parser.parse_args()
    scrapper(args.sites)
