from config.auto_config import MarineYamlConfig
import requests


class ConsoleRequest(MarineYamlConfig):
    def __init__(self):
        super(ConsoleRequest, self).__init__()

    def send_request(self, request_info_item):
        """
        向服务端发送请求
        """
        url = self.config["console_url"]
        resp = requests.post(url, data=request_info_item)
        if resp.status_code == 200:
            return True
        else:
            return False
