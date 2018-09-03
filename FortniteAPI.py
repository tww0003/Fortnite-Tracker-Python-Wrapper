import requests
import Stats
api_key = None


def get_stats(json):
    return Stats.FortniteStats(json)


class FortniteAPI:
    base_url = "https://api.fortnitetracker.com/v1/profile/"

    def __init__(self, platform, user):
        self.user = user
        self.platform = platform
        self.url = ""
        self.update_url()
        self.stats = None
        if api_key is not None:
            self.make_request()

    def set_user(self, user):
        self.user = user
        self.update_url()

    def set_platform(self, platform):
        self.platform = platform
        self.update_url()

    def update_url(self):
        self.url = self.base_url + self.platform + "/" + self.user
        if api_key is not None:
            self.make_request()

    def set_api_key(self, key):
        global api_key
        api_key = key
        self.make_request()

    def make_request(self):
        header = {"TRN-Api-Key": api_key}
        req = requests.get(self.url, headers=header)
        req.json()
        req.close()
        self.stats = get_stats(req.json())