import yaml
from datetime import datetime
import re
import os

__config = None
datetime.today().strftime("%d-%m-%Y")

current_date = datetime.today().strftime("%d-%m-%Y")
def config():
    import yaml
    global __config
    if not __config:
        with open('config.yaml', mode="r",) as f:
            __config = yaml.safe_load(f)
    return __config


def save(path, name, *args):
    if not os.path.exists(path):
        os.makedirs(path)
        with open(path + "/" + name, mode = "w") as f:
            for x in args:
                f.write(x)
                f.write("\n")


def set_name(title):
    title = title.strip()
    pattern = re.compile(r"[A-Za-z\s]+")
    res= "".join(pattern.findall(title))
    return res.replace(" ","-")+".txt"
    