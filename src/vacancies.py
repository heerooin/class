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

    def __it__(self, other):
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
    
class AbstractVacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, criteria):
        pass

class JSONSaver(AbstractVacancySaver):
    def __init__(self, file_path="vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a') as file:
            json.dump(vars(vacancy), file)
            file.write('\n')

    def delete_vacancy(self, vacancy):
        pass

    def get_vacancies_by_criteria(self, criteria):
        pass    