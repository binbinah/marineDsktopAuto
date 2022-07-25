# -*- coding: utf-8 -*-

import os
import platform
import yaml
from enum import Enum


class Action(Enum):

    STATUS = "status"
    LOGIN = "login"
    QUOTING = "quoting"
    BEST_PRICE = "best_price"
    NO_RESULT = "no_result"


class MarineYamlConfig(object):
    def __init__(
        self,
    ):
        self.path = os.path.abspath(os.path.dirname(__file__))
        self.config = self.yml_config()
        self.action_pair = {
            self.config["quoting_url"]: Action.QUOTING.value,
            self.config["cnc_line_url"]: Action.QUOTING.value,
            self.config["cnc_in"]: Action.QUOTING.value,
            self.config["best_price"]: Action.BEST_PRICE.value,
            self.config["no_result"]: Action.NO_RESULT.value,
        }
        self.cmd = "command" if platform.system() == "Darwin" else "ctrl"
        self.locate_address_keymap = (
            ["command", "l"] if platform.system() == "Darwin" else ["alt", "d"]
        )
        self.console_keymap = (
            ["command", "option", "j"]
            if platform.system() == "Darwin"
            else ["ctrl", "shift", "j"]
        )

    def yml_config(self):
        """读取 config.yml 的配置。"""
        with open(
            "/".join([self.path, "marine_config.yaml"]), "r", encoding="utf-8"
        ) as f:
            try:
                config = yaml.safe_load(f)
                return config
            except yaml.YAMLError as e:
                print("yml_config:{e}".format(e=e))
                return {}


if __name__ == "__main__":
    config = MarineYamlConfig()
    print(platform.system())
