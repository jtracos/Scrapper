import argparse

import yaml

from common import config
import logging
from scrapper import Scrapper

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    new_site_choices = list(config()['sites'].keys())
    parser.add_argument('sites',
                        help='Sitio del que desea minar las noticias',
                        type=str,
                        choices=new_site_choices)

    args = parser.parse_args()
    print(args.sites)
    scrapper = Scrapper(args.sites)
    scrapper()

help(yaml.load)