from FortniteAPI import FortniteAPI

FortniteAPI.api_key = 'fortnite_api_key'
api = FortniteAPI('xbl', 'tylerw330')

print('Solo kills per game: ' + str(api.stats.CURRENT_SOLO_KPG))
print('Duo kills per game: ' + str(api.stats.CURRENT_DUO_KPG))
print('Squad kills per game: ' + str(api.stats.CURRENT_SQUAD_KPG))
