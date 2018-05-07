import requests
from enum import Enum

api_key = None


class FortnitePlaylist(Enum):
    SOLO          = 'p2'
    DUO           = 'p10'
    SQUAD         = 'p9'
    CURRENT_SOLO  = 'curr_p2'
    CURRENT_DUO   = 'curr_p10'
    CURRENT_SQUAD = 'curr_p9'


class FortniteAPI:
    base_url = 'https://api.fortnitetracker.com/v1/profile/'

    def __init__(self, platform, user):
        self.user = user
        self.platform = platform
        self.url = ''
        self.update_url()
        self.json_data = None
        if api_key is not None:
            self.make_request()

    def set_user(self, user):
        self.user = user
        self.update_url()

    def set_platform(self, platform):
        self.platform = platform
        self.update_url()

    def update_url(self):
        self.url = self.base_url + self.platform + '/' + self.user
        if api_key is not None:
            self.make_request()

    def get_score(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['top10']['value']
        except KeyError:
            return_data = '0'
        return return_data

    def get_top_twelve(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['top12']['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_top_twenty_five(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['top25']['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_kd(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['kd']['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_matches(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['matches']['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_kills(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['kills']['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_kpg(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['kpg']['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_score_per_match(self, playlist):
        try:
            return_data = self.json_data['stats'][playlist.value]['scorePerMatch']['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_lifetime_score(self):
        try:
            return_data = self.json_data['lifeTimeStats'][6]['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_lifetime_matches_played(self):
        try:
            return_data = self.json_data['lifeTimeStats'][7]['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_lifetime_wins(self):
        try:
            return_data = self.json_data['lifeTimeStats'][8]['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_lifetime_win_percentage(self):
        try:
            return_data = self.json_data['lifeTimeStats'][9]['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_lifetime_kills(self):
        try:
            return_data = self.json_data['lifeTimeStats'][10]['value']
        except KeyError:
            return_data = '0'

        return return_data

    def get_lifetime_kd(self):
        try:
            return_data = self.json_data['lifeTimeStats'][11]['value']
        except KeyError:
            return_data = '0'

        return return_data

    def set_api_key(self, key):
        global api_key
        api_key = key
        self.make_request()

    def make_request(self):
        header = {'TRN-Api-Key': api_key}
        req = requests.get(self.url, headers=header)
        req.json()
        self.json_data = req.json()
        req.close()
