import yaml

__config = None


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
                  