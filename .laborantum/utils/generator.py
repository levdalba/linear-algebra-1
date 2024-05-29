import yaml
import os

def parse_item(fname):
    res = []
    with open(os.path.join(fname, 'config.yml'), 'r') as fin:
        config = yaml.safe_load(fin)
        if 'order' in config:
            for key in config['order']:
                res.extend(parse_item(os.path.join(fname, key)))
        if 'path' in config:
            return [config['path']]
    return res

res = parse_item('./texts')
print(res)