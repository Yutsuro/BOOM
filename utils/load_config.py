import yaml

class ConfigDict(dict): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.__dict__ = self


def load_config():

    config_path = "config.yaml"

    with open(config_path,encoding="utf8") as f:
        config = ConfigDict(yaml.safe_load(f)['config'])

    return config