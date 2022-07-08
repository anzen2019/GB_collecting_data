"""
Необходимо собрать информацию о вакансиях на вводимую должность
(используем input или через аргументы получаем должность) с сайтов HH(обязательно)
и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта
(также вводим через input или аргументы). Получившийся список должен содержать в себе
минимум:
- Наименование вакансии. Предлагаемую зарплату (разносим в три поля: минимальная и
максимальная и валюта. цифры преобразуем к цифрам).
- Ссылку на саму вакансию.
- Сайт, откуда собрана вакансия. (можно прописать статично hh.ru или superjob.ru)
По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести
с помощью dataFrame через pandas. Сохраните в json либо csv.
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from task_2_1_option import findSalary
import re
# url_test = 'https://hh.ru/search/vacancy?  text=python& from=suggest_post & salary=& clusters=true& ored_clusters=true&enable_snippets=true'
session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}
url = 'https://hh.ru'
vacancy_list = []
vacancy_request = input("Введите желаемый запрос вакансии: ")
params = {'search_field': 'name+description','text': vacancy_request}
response = session.get(url + '/search/vacancy', headers=headers, params=params)
dom = BeautifulSoup(response.text, 'html.parser')

""" 
>>> soup.select('[href="#internal"]')
# [<a href="#internal">Internal link</a>]"""
vacancies = dom.select('[class="vacancy-serp-item"]') #soup.select('[href="#internal"]')
#альтернативный вариант
# vacancies = dom.select('div.vacancy-serp-item')# поиск по тегу div, где атрибут vacancy-serp-item
pages = dom.findAll('a', {'data-qa': "pager-page"}) #исследуем номера страниц
last_page = (list(pages)[-1]).find('span').text #определили последнюю страницу
print(f'Всего страниц: {last_page}')

vacancies_data = [] #список с данными о компаниях
for page in range(1, int(last_page) + 2):
    params['page'] = page
    print(f'Сканирование страницы: {page}')
    response = session.get(url=url + '/search/vacancy', headers=headers, params=params)
    for vacancy in vacancies:
        vacancy_data = {} #словарь с данными для одной вакансии

        #внутри блока вакансии ищем заголовок с названием вакансии и компании:
        title_href = vacancy.find('a', {'data-qa': "vacancy-serp__vacancy-title"})
        company_href = vacancy.find('a', {'data-qa': "vacancy-serp__vacancy-employer"})

        # находим из этих блоков инфу о вакансии, компании:
        vacancy_data['Название вакансии'] = title_href.text
        vacancy_data['Ссылка'] = title_href.get('href')
        vacancy_data['Компания'] = company_href.text

        # ищем блок к з/п
        vacancy_data['Зарплата'] = findSalary(vacancy.find('span', {'data-qa': "vacancy-serp__vacancy-compensation"}))
        vacancy_data['Источник'] = url
        vacancies_data.append(vacancy_data)

pprint(vacancies_data)
print('Всего вакансий:' + str(len(vacancies_data)))