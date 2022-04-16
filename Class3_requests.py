import datetime
import requests
print(datetime.datetime.now())


def check_if_up(url):
    if requests.get(url).status_code != 200:
        print(f"{url} is up and running")
    else:
        print(f"sorry, {url} is down")


check_if_up("https://github.com")
