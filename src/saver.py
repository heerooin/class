import json
from abc import ABC, abstractmethod


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
        try:
            with open(self.file_path, 'r') as file:
                vacancies = [json.loads(line) for line in file if line.strip()]
            
            vacancies = [v for v in vacancies if v['name'] != vacancy.name]
            
            with open(self.file_path, 'w') as file:
                for v in vacancies:
                    json.dump(v, file)
                    file.write('\n')
        except FileNotFoundError:
            pass

    def get_vacancies_by_criteria(self, criteria):
        try:
            with open(self.file_path, 'r') as file:
                vacancies = [json.loads(line) for line in file if line.strip()]
            
            if not criteria:
                return vacancies
                
            filtered = []
            for vacancy in vacancies:
                if any(word.lower() in vacancy.get('name', '').lower() or 
                      word.lower() in vacancy.get('description', '').lower() 
                      for word in criteria):
                    filtered.append(vacancy)
            return filtered
        except FileNotFoundError:
            return []