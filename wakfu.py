#import urllib.parse
import requests

url_version = 'https://s.ankama.com/games/wakfu/gamedata/config.json'
version = requests.get(url_version).json()

currentTypes = {'actions', 'equipmentItemTypes', 'itemProperties', 'items', 'states'}

print('Select type:')
for t in currentTypes:
    print(t)
type = input()
print('Type selected: ' + type)

main_api = 'https://s.ankama.com/games/wakfu/gamedata/' + version['version'] + '/' + type + '.json'

json_data = requests.get(main_api).json()

for each in json_data:
    for item, value in each.items():
        print(item, value, end='\n')