import yaml


def load_config(configPath="./configs/config.yml"):
    f = open(configPath)
    config = yaml.load(f)
    f.close()
    return config
