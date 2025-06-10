import requests
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass

class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def get_vacancies(self, search_query):
        params = {"text": search_query, "area": 1}
        response = requests.get(self.url, headers=self.headers, params=params)
        return response.json()["items"]