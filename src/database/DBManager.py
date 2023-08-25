import psycopg2
from config import DB_CONNECTION_STRING
from config import EMPLOYERS_VACANCY_ID
from src.utils.import_queries import import_queries


class DBManager:

    def __init__(self) -> None:
        """Создаёт таблицы при их отсутствии и обновляет таблицу работодателей"""
        self.queries = import_queries()
        self.execute_query(self.queries['create table employers'])
        self.execute_query(self.queries['create table vacancies'])
        self.update_employers()

    def update_employers(self) -> None:
        """Загружает список работодателей из конфига и обновляет таблицу"""
        for emp_name, emp_id in EMPLOYERS_VACANCY_ID.items():
            try:
                self.execute_query(self.queries['update employers'], (emp_id, emp_name))
            except psycopg2.errors.UniqueViolation:
                pass

    def get_employers(self) -> dict:
        """Получает список работодателей из таблицы"""
        employers = {}
        resp = self.execute_query(self.queries['get employers'])
        for line in resp:
            employers[line[1]] = line[0]
        return employers

    def update_vacancies(self, vacancies):
        """
        Добавляет новые вакансии в таблицу
        :param vacancies: список найденных вакансий
        """

        for vacancy in vacancies:
            try:
                self.execute_query(self.queries['update vacancies'],
                                   (vacancy.company_id, vacancy.title, vacancy.salary['min'], vacancy.salary['max'],
                                    vacancy.salary['currency'], vacancy.url))
            except psycopg2.errors.UniqueViolation:
                pass

    def get_companies_and_vacancies_count(self) -> dict:
        """
        Получает список всех компаний и количество вакансий у каждой компании.

        :return: [{"company_name": number of vacancies}, {...}, ...]
        """

        number_of_vacancies = {}
        resp = self.execute_query(self.queries['count company vacancies'])
        for line in resp:
            number_of_vacancies[line[0]] = line[1]
        return number_of_vacancies

    def get_all_vacancies(self) -> list:
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию

        :return: [{"company_name": "name", "vacancy_name": "name", "salary_from": salary, "salary_to": salary,
        "url": "url"}, {...}, ...]
        """

        vacancies_data = []
        resp = self.execute_query(self.queries['get vacancies data'])
        for line in resp:
            data = {"company_name": line[0], "vacancy_name": line[1], "salary_from": line[2], "salary_to": line[3],
                    "url": line[4]}
            vacancies_data.append(data)

        return vacancies_data

    def get_avg_salary(self) -> float:
        """
        Получает среднюю зарплату по вакансиям

        :return: Среднее значение зарплаты
        """
        avg_salary = self.execute_query(self.queries['get avg salary'])
        return round(avg_salary)

    def get_vacancies_with_higher_salary(self) -> list:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям

        :return: [{"company_name": "name", "vacancy_name": "name", "salary": salary, "url": "url"}, {...}, ...]
        """
        vacancies_data = []
        resp = self.execute_query(self.queries['get vacancies with higher salary'])
        for line in resp:
            data = {"company_name": line[0], "vacancy_name": line[1], "salary_from": line[2], "salary_to": line[3],
                    "url": line[4]}
            vacancies_data.append(data)

        return vacancies_data

    def get_vacancies_with_keyword(self, keyword: str) -> list:
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова

        :param keyword: ключевое слово в названии вакансии
        :return: [{"company_name": "name", "vacancy_name": "name", "salary": salary, "url": "url"}, {...}, ...]
        """

        vacancies_data = []
        resp = self.execute_query(self.queries['get vacancies by keywords'], [f"%{keyword}%"])
        for line in resp:
            data = {"company_name": line[0], "vacancy_name": line[1], "salary_from": line[2], "salary_to": line[3],
                    "url": line[4]}
            vacancies_data.append(data)

        return vacancies_data

    @staticmethod
    def execute_query(query, params=None):
        """Выполняет SQL-запрос и возвращает ответ"""

        with psycopg2.connect(DB_CONNECTION_STRING) as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                try:
                    response = cur.fetchall()
                except psycopg2.ProgrammingError:
                    pass
            conn.commit()
        try:
            return response
        except UnboundLocalError:
            return None
