import requests


class FantasyFootballHub:
    def players_stats(self, token: str):
        URL = "https://data.fantasyfootballhub.co.uk/api/players-attack"

        PARAMS = {
            'mingw': 37,
            'maxgw': 37,
            'type': 'total',
            'venue': 'all',
            'season': 2021,
            'sortOn': 'points',
            'qty': 100,
            'sortOrder': 'desc',
            'playerSearch': '',
            'minCost': 0,
            'maxCost': 135,
            'positions': '1,2,3,4',
            'min_fdr': 1,
            'max_fdr': 5,
            'page_No': 1,
            'lowMins': False,
            'ppm': 0
        }

        HEADERS = {
            'Token': 'Bearer ' + token,
            'Authorization': 'r5C(e3.JeS^:_7LF'
        }

        response = requests.get(url=URL, params=PARAMS, headers=HEADERS)

        data = response.json()

        return data
