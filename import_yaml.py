import yaml

def open_keys(inputpath):
    with open(inputpath,'r') as f:
        keys = yaml.load(f, Loader=yaml.BaseLoader)
    return keys