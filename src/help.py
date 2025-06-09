def filter_vacancies(vacancies, criteria):
    """
    Фильтрует вакансии по ключевым словам
    """
    if not criteria:
        return vacancies
    
    filtered = []
    for vacancy in vacancies:
        if any(word.lower() in vacancy.get('name', '').lower() or 
               word.lower() in vacancy.get('description', '').lower() 
               for word in criteria):
            filtered.append(vacancy)
    return filtered

def get_vacancies_by_salary(vacancies, salary):
    if not salary:
        return vacancies
    final_salary = salary.split('-')
    if len(final_salary) == 1:
        min_salary = max_salary = int(final_salary[0])
    elif len(final_salary) == 2:
        min_salary, max_salary = map(int, final_salary)
    else:
        print("Неверный формат диапазона зарплат")
        return vacancies
    
    return [vacancy for vacancy in vacancies if
            vacancy.get('salary_from', 0) >= min_salary and vacancy.get('salary_from', float('inf')) <= max_salary]

def sort_vacancies(vacancies):
    return sorted(vacancies, key=lambda vacancy: vacancy.get('salary_from', 0), reverse=True)

def get_top_vacancies(vacancies, up):
    return vacancies[:up]

def print_vacancies(vacancies):
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"Вакансия {index}:")
            print(f"Название: {vacancy.get('name', 'Не указано')}")
            print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
    else:
        print("Нет подходящих вакансий")
