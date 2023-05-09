import json


def load_json(p):
    return json.loads(open(p, "r").read())


def json_files():
    return load_json("./data/db/车辆信息.json"), \
        load_json("./data/db/停车场信息.json"), \
        load_json("./data/db/停车记录.json")
