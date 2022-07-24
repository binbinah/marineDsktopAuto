from config.auto_config import MarineYamlConfig
import requests

class ConsoleRequest(MarineYamlConfig):
    def __init__(self):
        super(ConsoleRequest, self).__init__()

    def send_request(self, request_info_item):
        """
        像服务端发送请求
        :param request_info_item:
        :return:
        """
        pass
