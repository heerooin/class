import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


class vacancies:
    name: str
    url: str
    salary: int
    description: str

    def __init__(self, name, url, slary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description


if __name__ == '__main__':
    HH