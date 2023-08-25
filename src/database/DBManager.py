import psycopg2


class DBManager:
    def get_companies_and_vacancies_count(self) -> list:
        """
        Получает список всех компаний и количество вакансий у каждой компании.

        :return: [{"company_name": number of vacancies}, {...}, ...]
        """
        pass

    def get_all_vacancies(self) -> list:
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию

        :return: [{"company_name": "name", "vacancy_name": "name", "salary": salary, "url": "url"}, {...}, ...]
        """
        pass

    def get_avg_salary(self) -> float:
        """
        Получает среднюю зарплату по вакансиям

        :return: Среднее значение зарплаты
        """
        pass

    def get_vacancies_with_higher_salary(self) -> list:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям

        :return: [{"company_name": "name", "vacancy_name": "name", "salary": salary, "url": "url"}, {...}, ...]
        """
        pass

    def get_vacancies_with_keyword(self, keywords: list) -> list:
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова

        :param keywords: список ключевых слов, содержащихся в названии вакансии
        :return: [{"company_name": "name", "vacancy_name": "name", "salary": salary, "url": "url"}, {...}, ...]
        """
        pass
