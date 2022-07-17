import os
import yaml
from enum import Enum


class Action(Enum):

    STATUS = "status"
    LOGIN = "login"
    QUOTING = "quoting"


class MarineYamlConfig(object):
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__))
        self.config = self.yml_config()
        self.action_pair = {
            Action.STATUS.value: ''
        }

    def yml_config(self):
        """读取 config.yml 的配置。"""
        with open("/".join([self.path, "marine_config.yaml"]), "r") as f:
            try:
                config = yaml.safe_load(f)
                return config
            except yaml.YAMLError as e:
                print("yml_config:{e}".format(e=e))
                return {}


if __name__ == "__main__":
    config = MarineYamlConfig()
