"""
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""
import requests
from pprint import pprint
"""Вариант 1"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}
# params = { 'name' : 'johnplakon',
#             'appid' : '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'
#            }
username = 'alexandrei64'
token = "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"
repos = requests.get('https://api.github.com/users/'+username+'/repos', headers=headers, auth=(username, token))
#когда писал params = params - выдавалась ошибка аунтификации... почему тут не срабатывает params?
j_data = repos.json()
# pprint(j_data) #вывод всего - работает
# pprint(j_data.get('html_url')) #почему-то не работает
# pprint(j_data["html_url"]) #тоже не работает
with open('repo_list1.json', 'w', encoding='UTF-8') as file:
    for repo in repos.json():
        if not repo['private']:
            pprint(repo['html_url'])
            text = [repo['html_url'], '\n']
            file.writelines(text)


"""Вариант 2"""
username = input("Введите имя пользователя github: ")
repo = requests.get('https://api.github.com/users/'+username+'/repos')
j_data = repo.json()
with open('repo_list2.json', 'w', encoding='UTF-8') as file:
    for i in range(0,len(j_data)):
      project_name = j_data[i]['name']
      project_url = j_data[i]['svn_url']
      data = [f'Имя проекта: {project_name}, "\n"\
Ссылка на проект: {project_url}', '\n', '\n']
      print(project_name, project_url)
      file.writelines(data)


