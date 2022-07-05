"""
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""
# e5e4cd692a72b0b66ea0a6b80255d1c3
# import requests
# from pprint import pprint
#
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
# params = {'q': 'Chelyabinsk',
#           'appid': 'e5e4cd692a72b0b66ea0a6b80255d1c3'}
# url = 'https://api.openweathermap.org/data/2.5/weather'
#
# response = requests.get(url, headers=headers, params=params)
# j_data = response.json()
#
# pprint(f"Р’ РіРѕСЂРѕРґРµ {j_data.get('name')} С‚РµРјРїРµСЂР°С‚СѓСЂР° {round(j_data.get('main').get('temp') - 273.15, 2)} РіСЂР°РґСѓСЃРѕРІ")

import requests
# import os
from pprint import pprint
"""
Мой токен
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
"""
#мой код
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}
# params = { 'user_login' : 'anzen2019',
#            'appid' : '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'
#
# }

import os
username = 'natenka'
# token = os.environ.get("GITHUB_TOKEN")
token = "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"
repos = requests.get('https://api.github.com/user/repos', auth=(username, token))
r = requests.get('https://api.github.com/user', auth=(username, token))
with open('repo_list.json', 'w', encoding='UTF-8') as file:
    for repo in repos.json():
        if not repo['private']:
            print(repo['html_url'])
            text = [repo['html_url'], '\n']
            file.writelines(text)