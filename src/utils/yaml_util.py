import yaml
from src.consts.consts import Consts


def load(file_path: str):
    with open(file_path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)

config = load(Consts.DATA_CONFIG_DIR)
device_udid = config["user"]["username"]
#print(device_udid)

