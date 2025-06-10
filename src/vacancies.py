import json
from abc import ABC, abstractmethod

class Vacancies:
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description
        
        if not isinstance(self.salary, (str,int, float)):
            self.salary = 0

    def __lt__(self, other):
        return self.salary < other.salary
    
    def __eq__(self, other):
        return self.salary == other.salary
    
    def __gt__(self, other):
        return self.salary > other.salary
    
    def __str__(self):
        return f'Вакансия: {self.name}\n Ссылка: {self.url}\n Зарплата: {self.salary}\n Описание: {self.description}'
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Vacancies(data['name'], data['url'], data['salary'], data['description'])
