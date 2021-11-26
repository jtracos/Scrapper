import argparse
import yaml
from common import config
import logging
from scrapper import Scrapper

logger = logging.getLogger(__name__)

def start(uid):
    logging.info("comenzando minado en {}".format(uid))
    scrapper = Scrapper(uid)
    scrapper()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_site_choices = list(config()['sites'].keys())
    parser.add_argument('sites',
                        help='Sitio del que desea minar las noticias',
                        type=str,
                        choices=new_site_choices)

    args = parser.parse_args()
    start(args.sites)
