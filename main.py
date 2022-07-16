import pyautogui
import time
from service.marine_login import MarineLoginService
from service.marine_quoting import MarineQuotingService


def main():
    # login
    login_service = MarineLoginService()
    login_service.login_main()
    time.sleep(1)
    # goto quoting
    quoting_service = MarineQuotingService()
    quoting_service.quoting_main(quoting_service.config["departureFrom"])


if __name__ == "__main__":
    main()
